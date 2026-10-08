<#
  Vibe Editing OS - one-time installer (Windows 10/11, PowerShell 5.1+). No admin rights, nothing outside VEOS_HOME.
  Idempotent + resumable: every step checks what is already there. Re-run any time; use -Update to refresh the app.

  Params / env:
    -VeosHome   <dir>   VEOS_HOME (default %LOCALAPPDATA%\VibeEditingOS)
    -AppSource  <dir>   copy the app from a local checkout instead of git/zip (testing).  env VEOS_APP_SOURCE
    -Repo       <url>   GitHub repo (https://github.com/namansoniai/vibe-editing-os).   env VEOS_REPO
    -Ref        <name>  branch/tag (default main).                                        env VEOS_REF
    -Update             pull a new app version and reinstall the engine if it changed (skips big downloads that exist)
    -SkipModels         skip the ~1.7 GB model downloads (doctor will report them missing)
    env VEOS_LICENCE_KEY    activate this licence key right after the engine step (before the big downloads); a
                            rejected key stops the install with step "licence" and licence_error = the engine's code
  Output: one progress line per step ("[n/10] ..."), final line is JSON {"ok":true|false,...}. Log: VEOS_HOME\install.log
#>
param(
  [Alias('Home')][string]$VeosHome = $(if ($env:VEOS_HOME) { $env:VEOS_HOME } else { Join-Path $env:LOCALAPPDATA 'VibeEditingOS' }),
  [string]$AppSource = $env:VEOS_APP_SOURCE,
  [string]$Repo = $env:VEOS_REPO,
  [string]$Ref = $(if ($env:VEOS_REF) { $env:VEOS_REF } else { 'main' }),
  [switch]$Update,
  [switch]$SkipModels
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}
Add-Type -AssemblyName System.IO.Compression.FileSystem

# ---- pinned toolchain (docs/BENCHMARKS.md "Toolchain (Phase 0.2)") --------------------------------------------------
$UV_VERSION   = '0.12.23'
$FFMPEG_TAG   = 'autobuild-2026-10-03-18-14'
$FFMPEG_NAME  = 'ffmpeg-N-127142-g12b7b9891b-win64-gpl'
$FFMPEG_URL   = "https://github.com/BtbN/FFmpeg-Builds/releases/download/$FFMPEG_TAG/$FFMPEG_NAME.zip"
$FFMPEG_SHA   = 'a885f564dee2b60f69ab866c6c89b96ae531fc2ee1f24ff8b5b1a6d29960a96b'
$RVM_URL      = 'https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx'
$YUNET_URL    = 'https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx'
$YUNET_SHA    = '8f2383e4dd3cfbb4553ea8718107fc0423210dc964f9f4280604804ed2552fa4'
$FACE_URL     = 'https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite'
$WHISPER_REPO = 'mobiuslabsgmbh/faster-whisper-large-v3-turbo'
# speaker labels for multi-speaker reels (no account/token): pyannote segmentation-3.0 (MIT) + CAM++ (Apache-2.0)
$SPKSEG_URL   = 'https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-segmentation-models/sherpa-onnx-pyannote-segmentation-3-0.tar.bz2'
$SPKSEG_SHA   = '24615ee884c897d9d2ba09bb4d30da6bb1b15e685065962db5b02e76e4996488'
$SPKEMB_URL   = 'https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/3dspeaker_speech_campplus_sv_en_voxceleb_16k.onnx'
$SPKEMB_SHA   = '357a834f702b80161e5b981182c038e18553c1f2ca752ed6cec2052365d4129b'
$TOTAL = 10

$Home_ = [IO.Path]::GetFullPath($VeosHome)
$T0 = Get-Date
$script:Step = 'start'
$script:N = 0
New-Item -ItemType Directory -Force -Path $Home_ | Out-Null
$LogFile = Join-Path $Home_ 'install.log'
$Dl = Join-Path $Home_ 'scratch\downloads'
$App = Join-Path $Home_ 'app'
$Tools = Join-Path $Home_ 'tools'
$Venv = Join-Path $Home_ 'venv'
$VenvPy = Join-Path $Venv 'Scripts\python.exe'
$Uv = Join-Path $Tools 'uv\uv.exe'
$State = Join-Path $Home_ 'state'
New-Item -ItemType Directory -Force -Path $Dl, $State | Out-Null

function Log([string]$m) { try { Add-Content -Path $LogFile -Value ("{0} {1}" -f (Get-Date -Format s), $m) } catch {} }
function Step([string]$name, [string]$label) {
  $script:Step = $name; $script:N++
  $line = "[{0}/{1}] {2}" -f $script:N, $TOTAL, $label
  Write-Host $line; Log $line
}
function Info([string]$m) { Write-Host "      $m"; Log "      $m" }
function MB([long]$b) { '{0:N0} MB' -f ($b / 1MB) }

function Download([string]$url, [string]$out, [string]$sha = '') {
  $dir = Split-Path $out -Parent; New-Item -ItemType Directory -Force -Path $dir | Out-Null
  for ($i = 1; $i -le 3; $i++) {
    try {
      if (Test-Path $out) { Remove-Item $out -Force }
      Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
      $len = (Get-Item $out).Length
      if ($sha) {
        $got = (Get-FileHash -Algorithm SHA256 -Path $out).Hash.ToLower()
        if ($got -ne $sha.ToLower()) { throw "sha256 mismatch for $(Split-Path $out -Leaf): expected $sha got $got" }
      }
      Info ("downloaded {0} ({1})" -f (Split-Path $out -Leaf), (MB $len))
      return
    } catch {
      Log "download attempt $i failed: $($_.Exception.Message)"
      if ($i -eq 3) { throw "download failed after 3 tries: $url ($($_.Exception.Message))" }
      Info "network hiccup, retrying ($i/3)..."; Start-Sleep -Seconds (3 * $i)
    }
  }
}
function Run([string]$exe, [string[]]$argv) {
  Log ("RUN {0} {1}" -f $exe, ($argv -join ' '))
  & $exe @argv
  if ($LASTEXITCODE -ne 0) { throw "$(Split-Path $exe -Leaf) exited with code $LASTEXITCODE" }
}
function Retry([scriptblock]$sb, [string]$what) {
  for ($i = 1; $i -le 3; $i++) {
    try { & $sb; return } catch {
      Log "$what attempt $i failed: $($_.Exception.Message)"
      if ($i -eq 3) { throw }
      Info "$what failed, retrying ($i/3)..."; Start-Sleep -Seconds (3 * $i)
    }
  }
}
function Unzip([string]$zip, [string]$dest) {
  if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
  [IO.Compression.ZipFile]::ExtractToDirectory($zip, $dest)
}
function HashOf([string[]]$files) {
  $sb = New-Object System.Text.StringBuilder
  foreach ($f in $files) { if (Test-Path $f) { [void]$sb.Append((Get-FileHash -Algorithm SHA256 -Path $f).Hash) } }
  return $sb.ToString()
}
function Finish([bool]$ok, [hashtable]$extra) {
  $o = [ordered]@{ ok = $ok; home = $Home_; seconds = [int]((Get-Date) - $T0).TotalSeconds; log = $LogFile }
  foreach ($k in $extra.Keys) { $o[$k] = $extra[$k] }
  Write-Output ($o | ConvertTo-Json -Compress -Depth 6)
  if ($ok) { exit 0 } else { exit 1 }
}

# Process-scoped env only (never touches the user/system environment).
$env:VEOS_HOME = $Home_
$env:UV_PYTHON_INSTALL_DIR = Join-Path $Home_ 'python'
$env:UV_CACHE_DIR = Join-Path $Home_ 'cache\uv'
$env:UV_PYTHON_PREFERENCE = 'only-managed'
$env:UV_LINK_MODE = 'copy'
$env:UV_NO_PROGRESS = '1'
$env:PLAYWRIGHT_BROWSERS_PATH = Join-Path $Home_ 'browsers'
$env:HF_HOME = Join-Path $Home_ 'models\hf'
$env:HF_HUB_DISABLE_SYMLINKS_WARNING = '1'
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
$env:GIT_TERMINAL_PROMPT = '0'

$hint = @{
  home = 'Check that the folder is writable and the disk has about 5 GB free.'
  app = 'Check your internet connection. For a private repo, make sure git is installed and signed in to GitHub (git credential manager), then re-run.'
  uv = 'Check your internet connection / proxy and re-run; the installer resumes where it stopped.'
  python = 'Check your internet connection and re-run.'
  engine = 'Re-run the installer. If it persists, send the last lines of install.log.'
  ffmpeg = 'Check your internet connection and re-run (the download is checksum-verified).'
  browser = 'Check your internet connection and re-run.'
  models = 'Check your internet connection and re-run; finished downloads are kept.'
  playbooks = 'Check that VEOS_HOME is writable.'
  doctor = 'Run `veos doctor` and follow the hint on the failing check.'
}

try {
  # ---- 1 home --------------------------------------------------------------------------------------------------
  Step 'home' "Preparing $Home_"
  foreach ($d in 'tools', 'browsers', 'models\rvm', 'models\mediapipe', 'models\yunet', 'models\hf', 'playbooks', 'scratch', 'cache', 'sfx') {  # sfx = on-demand sound cache (veos sfx fetch)
    New-Item -ItemType Directory -Force -Path (Join-Path $Home_ $d) | Out-Null
  }

  # ---- 2 app ---------------------------------------------------------------------------------------------------
  Step 'app' 'Getting the Vibe Editing OS app (engine, renderer, playbooks, assets)'
  $appDirs = 'engine', 'renderer', 'playbooks', 'assets'
  $before = HashOf @((Join-Path $App 'engine\pyproject.toml'), (Join-Path $App 'engine\uv.lock'))
  if ($AppSource) {
    $src = (Resolve-Path $AppSource).Path
    Info "copying from local source $src"
    foreach ($d in $appDirs) {
      $s = Join-Path $src $d; $t = Join-Path $App $d
      if (-not (Test-Path $s)) { throw "$s not found in -AppSource" }
      & robocopy $s $t /MIR /NFL /NDL /NJH /NJS /NP /XD .git __pycache__ .pytest_cache .venv node_modules inspiration /XF *.mp4 *.mov *.mkv *.wav *.m4a *.onnx *.bin | Out-Null
      if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($d) code $LASTEXITCODE" }
    }
    $global:LASTEXITCODE = 0
  } else {
    if (-not $Repo) { $Repo = 'https://github.com/namansoniai/vibe-editing-os-dist' }
    if (-not $Repo) {
      $pj = Join-Path $PSScriptRoot '..\.claude-plugin\plugin.json'
      if (Test-Path $pj) { try { $Repo = (Get-Content $pj -Raw | ConvertFrom-Json).repository } catch {} }
    }
    if (-not $Repo -or $Repo -match 'OWNER') { throw "repository not configured: set VEOS_REPO=https://github.com/<owner>/vibe-editing-os (or -AppSource <checkout>)" }
    if ($Repo -notmatch '^https?://') { $Repo = "https://github.com/$Repo" }
    $Repo = $Repo.TrimEnd('/'); if ($Repo.EndsWith('.git')) { $Repo = $Repo.Substring(0, $Repo.Length - 4) }
    $git = Get-Command git -ErrorAction SilentlyContinue
    $done = $false
    if ($git) {
      try {
        if (Test-Path (Join-Path $App '.git')) {
          Info "git: updating existing checkout ($Ref)"
          Retry { Run 'git' @('-C', $App, 'fetch', '--depth', '1', 'origin', $Ref) } 'git fetch'
          Run 'git' @('-C', $App, 'reset', '--hard', 'FETCH_HEAD')
        } else {
          if (Test-Path $App) { Remove-Item $App -Recurse -Force }
          Info "git: cloning $Repo ($Ref) - uses your git credentials, so private repos work"
          Retry {
            if (Test-Path $App) { Remove-Item $App -Recurse -Force }
            Run 'git' @('clone', '--depth', '1', '--branch', $Ref, '--filter=blob:none', '--sparse', $Repo, $App)
            Run 'git' (@('-C', $App, 'sparse-checkout', 'set') + $appDirs)
          } 'git clone'
        }
        $done = $true
      } catch { Info "git route failed ($($_.Exception.Message)); trying the zip download"; if (Test-Path (Join-Path $App '.git')) { } }
    }
    if (-not $done) {
      $slug = ($Repo -replace '^https?://github.com/', '')
      $zipUrl = "https://codeload.github.com/$slug/zip/refs/heads/$Ref"
      $z = Join-Path $Dl 'app.zip'; $x = Join-Path $Dl 'app-x'
      Download $zipUrl $z
      Unzip $z $x
      $top = Get-ChildItem $x | Select-Object -First 1
      if (Test-Path $App) { Remove-Item $App -Recurse -Force }
      New-Item -ItemType Directory -Force -Path $App | Out-Null
      foreach ($d in $appDirs) { Copy-Item -Recurse -Force (Join-Path $top.FullName $d) (Join-Path $App $d) }
      Remove-Item $z, $x -Recurse -Force
    }
  }
  foreach ($d in $appDirs) { if (-not (Test-Path (Join-Path $App $d))) { throw "app is incomplete: $d missing" } }
  $after = HashOf @((Join-Path $App 'engine\pyproject.toml'), (Join-Path $App 'engine\uv.lock'))
  Info ("app ready at {0}" -f $App)

  # ---- 3 uv ----------------------------------------------------------------------------------------------------
  Step 'uv' "uv $UV_VERSION (Python manager)"
  $uvOk = $false
  if (Test-Path $Uv) { try { $uvOk = ((& $Uv --version) -match [regex]::Escape($UV_VERSION)) } catch {} }
  if ($uvOk) { Info 'already installed' } else {
    $arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'aarch64' } else { 'x86_64' }
    $asset = "uv-$arch-pc-windows-msvc.zip"
    $base = "https://github.com/astral-sh/uv/releases/download/$UV_VERSION/$asset"
    $z = Join-Path $Dl $asset
    $shaTxt = (Invoke-WebRequest -Uri "$base.sha256" -UseBasicParsing).Content
    if ($shaTxt -is [byte[]]) { $shaTxt = [Text.Encoding]::UTF8.GetString($shaTxt) }
    $sha = ($shaTxt.Trim() -split '\s+')[0]
    Download $base $z $sha
    $x = Join-Path $Dl 'uv-x'; Unzip $z $x
    New-Item -ItemType Directory -Force -Path (Join-Path $Tools 'uv') | Out-Null
    $exe = Get-ChildItem $x -Recurse -Filter uv.exe | Select-Object -First 1
    Copy-Item (Join-Path $exe.DirectoryName '*') (Join-Path $Tools 'uv') -Force
    Remove-Item $z, $x -Recurse -Force
  }
  if (-not (Test-Path $Uv)) { throw 'uv.exe missing after install' }

  # ---- 4 python + venv -----------------------------------------------------------------------------------------
  Step 'python' 'Python 3.12 + virtual environment (~70 MB)'
  Retry { Run $Uv @('python', 'install', '3.12') } 'python download'
  if (-not (Test-Path $VenvPy)) { Run $Uv @('venv', $Venv, '--python', '3.12') } else { Info 'venv already exists' }

  # ---- 5 engine ------------------------------------------------------------------------------------------------
  Step 'engine' 'Installing the veos engine and its packages (~700 MB)'
  $stamp = Join-Path $State 'engine.sha'
  $have = if (Test-Path $stamp) { (Get-Content $stamp -Raw).Trim() } else { '' }
  # Always sync to EXACTLY the locked set (removes extras, restores changed versions); a no-op when already matching.
  $req = Join-Path $Dl 'requirements.txt'
  Run $Uv @('export', '--project', (Join-Path $App 'engine'), '--frozen', '--no-dev', '--no-emit-project', '--no-hashes', '-o', $req, '-q')
  Retry { Run $Uv @('pip', 'sync', '--python', $VenvPy, $req) } 'package sync'
  # editable: the engine locates renderer/, assets/, playbooks/ relative to app/engine/src, so it must run from app/
  Retry { Run $Uv @('pip', 'install', '--python', $VenvPy, '--no-deps', '-e', (Join-Path $App 'engine')) } 'engine install'
  Remove-Item $req -Force -ErrorAction SilentlyContinue
  Set-Content -Path $stamp -Value $after -Encoding ascii

  # licence: activate as soon as the engine exists, before the big downloads (key from the setup skill, env only)
  if ($env:VEOS_LICENCE_KEY) {
    $script:Step = 'licence'
    Info 'activating your licence'
    $lic = & $VenvPy -m veos licence activate --key $env:VEOS_LICENCE_KEY
    $global:LASTEXITCODE = 0
    $lj = $null; try { $lj = (@($lic) | Select-Object -Last 1) | ConvertFrom-Json } catch {}
    if (-not $lj -or -not $lj.ok) {
      $le = if ($lj) { $lj.error } else { @{ code = 'UNEXPECTED'; message = "licence activation gave no answer: $lic"; hint = 'Re-run setup.' } }
      Log "licence activation failed: $($le.code)"
      Write-Host "FAILED at step 'licence': $($le.message)"
      Finish $false @{ step = 'licence'; licence_error = $le.code; error = $le.message; hint = $le.hint }
    }
    Info $lj.message
    $script:Step = 'engine'
  }

  # ---- 6 ffmpeg ------------------------------------------------------------------------------------------------
  Step 'ffmpeg' 'ffmpeg (pinned BtbN build, ~150 MB, checksum-verified)'
  $ffDir = Join-Path $Tools 'ffmpeg'; $ffVer = Join-Path $ffDir 'VERSION'
  if ((Test-Path (Join-Path $ffDir 'bin\ffmpeg.exe')) -and (Test-Path (Join-Path $ffDir 'bin\ffprobe.exe'))) {
    Info 'already installed'
  } else {
    $z = Join-Path $Dl "$FFMPEG_NAME.zip"
    Download $FFMPEG_URL $z $FFMPEG_SHA
    $x = Join-Path $Dl 'ffmpeg-x'; Unzip $z $x
    $inner = Get-ChildItem $x | Select-Object -First 1
    if (Test-Path $ffDir) { Remove-Item $ffDir -Recurse -Force }
    Move-Item $inner.FullName $ffDir
    Set-Content -Path $ffVer -Value "$FFMPEG_TAG $FFMPEG_NAME" -Encoding ascii
    Remove-Item $z, $x -Recurse -Force -ErrorAction SilentlyContinue
  }

  # ---- 7 chromium ----------------------------------------------------------------------------------------------
  Step 'browser' 'Chromium for rendering (Playwright, ~350 MB)'
  Retry { Run $VenvPy @('-m', 'playwright', 'install', 'chromium') } 'chromium download'

  # ---- 8 models ------------------------------------------------------------------------------------------------
  Step 'models' 'AI models: background matte (~14 MB), face detector (~1 MB), speaker labels (~34 MB), speech-to-text whisper turbo (~1.6 GB)'
  if ($SkipModels) { Info 'skipped (-SkipModels)' } else {
    $rvm = Join-Path $Home_ 'models\rvm\rvm_mobilenetv3_fp32.onnx'
    if (-not (Test-Path $rvm)) { Download $RVM_URL "$rvm.part"; Move-Item "$rvm.part" $rvm -Force } else { Info 'RVM already present' }
    $face = Join-Path $Home_ 'models\mediapipe\blaze_face_short_range.tflite'
    if (-not (Test-Path $face)) { Download $FACE_URL "$face.part"; Move-Item "$face.part" $face -Force } else { Info 'face model already present' }
    $yn = Join-Path $Home_ 'models\yunet\face_detection_yunet_2023mar.onnx'
    if ((Test-Path $yn) -and ((Get-FileHash -Algorithm SHA256 -Path $yn).Hash.ToLower() -ne $YUNET_SHA)) { Remove-Item $yn -Force }
    if (-not (Test-Path $yn)) { Download $YUNET_URL "$yn.part" $YUNET_SHA; Move-Item "$yn.part" $yn -Force } else { Info 'YuNet face model already present' }
    $spk = Join-Path $Home_ 'models\diarize'; New-Item -ItemType Directory -Force -Path $spk | Out-Null
    $seg = Join-Path $spk 'pyannote-segmentation-3.0.onnx'
    if (-not (Test-Path $seg)) {
      $tb = Join-Path $Dl 'spk-seg.tar.bz2'; Download $SPKSEG_URL $tb $SPKSEG_SHA
      $tx = Join-Path $Dl 'spk-seg'; New-Item -ItemType Directory -Force -Path $tx | Out-Null
      & tar -xjf $tb -C $tx; if ($LASTEXITCODE -ne 0) { throw 'could not unpack the speaker segmentation model' }
      $sd = Get-ChildItem $tx -Recurse -Filter model.onnx | Select-Object -First 1
      Copy-Item $sd.FullName $seg -Force
      Copy-Item (Join-Path $sd.DirectoryName 'LICENSE') (Join-Path $spk 'pyannote-segmentation-3.0.LICENSE.txt') -Force -ErrorAction SilentlyContinue
      Remove-Item $tb, $tx -Recurse -Force -ErrorAction SilentlyContinue
    } else { Info 'speaker segmentation model already present' }
    $emb = Join-Path $spk 'campplus_sv_en_voxceleb_16k.onnx'
    if (-not (Test-Path $emb)) { Download $SPKEMB_URL "$emb.part" $SPKEMB_SHA; Move-Item "$emb.part" $emb -Force } else { Info 'speaker embedding model already present' }
    Info 'whisper turbo: downloading (resumes if interrupted; this is the long one)'
    $py = @"
from huggingface_hub import snapshot_download
p = snapshot_download('$WHISPER_REPO', allow_patterns=['config.json','preprocessor_config.json','model.bin','tokenizer.json','vocabulary.*'])
print(p)
"@
    $pyFile = Join-Path $Dl 'prefetch_whisper.py'
    Set-Content -Path $pyFile -Value $py -Encoding ascii
    Retry { Run $VenvPy @($pyFile) } 'whisper download'
  }

  # ---- 9 playbooks ---------------------------------------------------------------------------------------------
  Step 'playbooks' 'Your playbooks folder (templates only; the reference stays read-only in app/)'
  $pbRoot = Join-Path $Home_ 'playbooks'
  foreach ($pb in '_template', '_styles') {
    $s = Join-Path $App "playbooks\$pb"; $t = Join-Path $pbRoot $pb
    if ((Test-Path $s) -and -not (Test-Path $t)) { Copy-Item -Recurse $s $t; Info "copied $pb" }
  }

  # ---- 10 doctor -----------------------------------------------------------------------------------------------
  Step 'doctor' 'Checking everything with veos doctor'
  $env:PATH = (Join-Path $Home_ 'tools\ffmpeg\bin') + ';' + $env:PATH
  $doc = & $VenvPy -m veos doctor
  $global:LASTEXITCODE = 0
  $ready = $false; $problems = @()
  try { $j = ($doc | Out-String) | ConvertFrom-Json; $ready = [bool]$j.ready; $problems = @($j.problems) } catch { $problems = @("doctor output unreadable: $doc") }
  Info $(if ($ready) { 'doctor: ready' } else { 'doctor: problems found' })
  Remove-Item $Dl -Recurse -Force -ErrorAction SilentlyContinue
  Remove-Item (Join-Path $Home_ 'cache') -Recurse -Force -ErrorAction SilentlyContinue  # uv download cache (~800 MB), not needed after install

  $size = (Get-ChildItem $Home_ -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  Finish $true @{ doctor_ready = $ready; problems = $problems; size_mb = [int]($size / 1MB); app = $App; venv = $Venv }
} catch {
  $msg = $_.Exception.Message
  Log "FAILED at $script:Step : $msg"
  Write-Host "FAILED at step '$script:Step': $msg"
  Finish $false @{ step = $script:Step; error = $msg; hint = $hint[$script:Step] }
}
