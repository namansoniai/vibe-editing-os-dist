<#
  Vibe Editing OS - one-time installer (Windows 10/11, PowerShell 5.1+). No admin rights; nothing outside VEOS_HOME except
  VEOS_HOME\bin (the `veos` wrapper) added once to the USER Path, so `veos` works in any new PowerShell or cmd window.
  Everything it downloads, caches or unpacks (uv, Python, packages, Chromium, models, temp files) stays inside VEOS_HOME.
  Idempotent + resumable: every step checks what is already there. Re-run any time; use -Update to refresh the app.

  Params / env:
    -VeosHome   <dir>   VEOS_HOME (env VEOS_HOME). Default: %USERPROFILE%\VibeEditingOS if it exists, else the 0.6.0 folder
                        %LOCALAPPDATA%\VibeEditingOS if it holds an engine, else %USERPROFILE%\VibeEditingOS. Not in AppData:
                        the Claude desktop app is an MSIX package and Windows redirects its AppData writes, which broke uv.
    -AppSource  <dir>   copy the app from a local checkout instead of the app zip (testing). env VEOS_APP_SOURCE
    -Repo       <url>   override the GitHub repo of the app zip (default: plugin.json "repository"). env VEOS_REPO
    -Update             download the app again and resync the engine (skips big downloads that exist)
                        The app is always the zip of THIS plugin's version (setup/release.json from the dist build,
                        sha256-pinned), so the engine and the skills never drift apart. No git anywhere.
    -SkipModels         skip the ~1.7 GB model downloads (doctor will report them missing)
    env VEOS_LICENCE_KEY    activate this licence key right after the engine step (before the big downloads); a
                            rejected key stops the install with step "licence" and licence_error = the engine's code.
                            An unreachable licence server (LICENCE_OFFLINE) never stops it: the downloads go on, the
                            activation is tried again at the end, and if it still fails the result is ok with
                            licence_pending = true (setup activates later).
  Output: one progress line per step ("[n/10] ..."), final line is JSON {"ok":true|false,...}. Log: VEOS_HOME\install.log
#>
param(
  [Alias('Home')][string]$VeosHome = $env:VEOS_HOME,
  [string]$AppSource = $env:VEOS_APP_SOURCE,
  [string]$Repo = $env:VEOS_REPO,
  [switch]$Update,
  [switch]$SkipModels
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}
Add-Type -AssemblyName System.IO.Compression.FileSystem

# ---- pinned toolchain (docs/BENCHMARKS.md "Toolchain (Phase 0.2)") --------------------------------------------------
$UV_VERSION   = '0.12.23'
# ffmpeg: a stable release, gyan.dev "essentials" (static win64: libx264, aac, libwebp, png/mjpeg and every built-in filter
# the engine uses). The GitHub release tag never expires; gyan.dev serves the identical file (same sha256) as a mirror.
$FFMPEG_VERSION = '9.0.2'
$FFMPEG_NAME  = "ffmpeg-$FFMPEG_VERSION-essentials_build"
$FFMPEG_URLS  = @("https://github.com/GyanD/codexffmpeg/releases/download/$FFMPEG_VERSION/$FFMPEG_NAME.zip",
                  "https://www.gyan.dev/ffmpeg/builds/packages/$FFMPEG_NAME.zip")
$FFMPEG_SHA   = '60f467265b1e312373dbcd92200c2618a74850f98d3d078e94296bb3fa2047ba'
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

# ---- BEGIN home: where VEOS_HOME is + the process env (engine/tests/test_home.py runs this block on its own) ---------
# Same order as the engine's core.veos_home and plugin/bin/veos(.cmd), so the installer and the engine always agree.
function Get-VeosHomes {
  $prof = if ($env:USERPROFILE) { $env:USERPROFILE } else { [Environment]::GetFolderPath('UserProfile') }
  $local = if ($env:LOCALAPPDATA) { $env:LOCALAPPDATA } else { Join-Path $prof 'AppData\Local' }
  return @((Join-Path $prof 'VibeEditingOS'), (Join-Path $local 'VibeEditingOS'))  # new, legacy (0.6.0 and earlier)
}
function Test-VeosEngine([string]$h) {
  return ((Test-Path -LiteralPath (Join-Path $h 'venv\Scripts\python.exe') -PathType Leaf) -or
          (Test-Path -LiteralPath (Join-Path $h 'dev-venv\Scripts\python.exe') -PathType Leaf))
}
function Resolve-VeosHome {
  if ($env:VEOS_HOME) { return $env:VEOS_HOME }
  $new, $legacy = Get-VeosHomes
  if ((Test-Path -LiteralPath $new) -or -not (Test-VeosEngine $legacy)) { return $new }
  return $legacy
}
# Process-scoped env only (the user Path gets VEOS_HOME\bin in step 10, nothing else). Every download / cache / scratch
# folder of uv, pip, Playwright, Hugging Face, torch and the temp dir points inside VEOS_HOME, never AppData or %TEMP%.
function Set-VeosEnv([string]$h) {
  $tmp = Join-Path $h 'tmp'; New-Item -ItemType Directory -Force -Path $tmp | Out-Null
  $e = [ordered]@{
    VEOS_HOME = $h
    UV_PYTHON_INSTALL_DIR = Join-Path $h 'python'; UV_PYTHON_BIN_DIR = Join-Path $h 'python\bin'
    UV_PYTHON_INSTALL_BIN = '0'; UV_PYTHON_INSTALL_REGISTRY = '0'  # no python.exe in ~\.local\bin, no registry entries
    UV_CACHE_DIR = Join-Path $h 'cache\uv'; UV_TOOL_DIR = Join-Path $h 'tools\uv-tools'; UV_TOOL_BIN_DIR = Join-Path $h 'tools\uv-tools\bin'
    UV_PYTHON_PREFERENCE = 'only-managed'; UV_LINK_MODE = 'copy'; UV_NO_PROGRESS = '1'; UV_HTTP_TIMEOUT = '120'
    UV_SYSTEM_CERTS = '1'; NODE_USE_SYSTEM_CA = '1'  # trust the Windows certificate store (antivirus / office proxy roots)
    PIP_CACHE_DIR = Join-Path $h 'cache\pip'
    PLAYWRIGHT_BROWSERS_PATH = Join-Path $h 'browsers'
    HF_HOME = Join-Path $h 'models\hf'; TORCH_HOME = Join-Path $h 'models\torch'; MPLCONFIGDIR = Join-Path $h 'cache\matplotlib'
    HF_HUB_DISABLE_SYMLINKS_WARNING = '1'
    TMP = $tmp; TEMP = $tmp
    PYTHONIOENCODING = 'utf-8'; PYTHONUTF8 = '1'
  }
  foreach ($k in $e.Keys) { Set-Item -Path "env:$k" -Value $e[$k] }
  return $e
}
# Earlier installs run from inside the Claude desktop app (an MSIX package) that Windows redirected out of %LOCALAPPDATA%.
function Find-PackageRedirect {
  if (-not $env:LOCALAPPDATA) { return @() }
  $pk = Join-Path $env:LOCALAPPDATA 'Packages'
  if (-not (Test-Path -LiteralPath $pk)) { return @() }
  return @(Get-ChildItem -LiteralPath $pk -Directory -Filter 'Claude_*' -ErrorAction SilentlyContinue |
    ForEach-Object { Join-Path $_.FullName 'LocalCache\Local\VibeEditingOS' } | Where-Object { Test-Path -LiteralPath $_ })
}
# ---- END home --------------------------------------------------------------------------------------------------------

# ---- BEGIN preflight: checks before any download (engine/tests/test_install_scripts.py runs this block on its own) --
# Which Python to install on this PC, or why it can't run. Every engine wheel exists for win_amd64 but not win_arm64, so
# ARM PCs get the x64 Python (Windows 11 runs it under its built-in emulation; Windows 10 on ARM can't run x64 apps).
function Get-PlatformPlan([string]$arch, [int]$build) {
  if ($arch -eq 'ARM64') {
    if ($build -lt 22000) {
      return @{ ok = $false; msg = "This PC isn't supported yet: on ARM PCs Vibe Editing OS needs Windows 11 (Windows 10 on ARM can't run its 64-bit video tools)." }
    }
    return @{ ok = $true; arm = $true; python = 'cpython-3.12-windows-x86_64-none' }
  }
  if ($arch -ne 'AMD64') { return @{ ok = $false; msg = "This PC isn't supported: Vibe Editing OS needs 64-bit Windows 10 or 11." } }
  return @{ ok = $true; arm = $false; python = 'cpython-3.12-windows-x86_64-none' }
}
function Get-MachineArch {
  $a = @($env:PROCESSOR_ARCHITEW6432, $env:PROCESSOR_ARCHITECTURE)
  try { $a += (Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name PROCESSOR_ARCHITECTURE -ErrorAction Stop).PROCESSOR_ARCHITECTURE } catch {}
  if ($a -contains 'ARM64') { return 'ARM64' }
  if ($a -contains 'AMD64') { return 'AMD64' }
  return [string]$env:PROCESSOR_ARCHITECTURE
}
function Get-FreeGB([string]$path) {
  try { return [math]::Round((New-Object IO.DriveInfo ([IO.Path]::GetPathRoot($path))).AvailableFreeSpace / 1GB, 1) } catch { return $null }
}
# One installer at a time: the lock is an open file handle (no other process can open it for writing), so it is released
# automatically when the installer exits, even if it crashed or the window was closed.
function Lock-Install([string]$lock) {
  try { $s = [IO.File]::Open($lock, [IO.FileMode]::OpenOrCreate, [IO.FileAccess]::ReadWrite, [IO.FileShare]::Read) } catch { return $null }
  $b = [Text.Encoding]::ASCII.GetBytes(("pid {0} started {1}" -f $PID, (Get-Date -Format s)))
  $s.SetLength(0); $s.Write($b, 0, $b.Length); $s.Flush()
  return $s
}
function Get-RunningStep([string]$log) {
  try { $m = @(Select-String -LiteralPath $log -Pattern '\[(\d+/\d+)\]' -ErrorAction Stop | Select-Object -Last 1); if ($m) { return $m[0].Matches[0].Groups[1].Value } } catch {}
  return ''
}
# ---- END preflight ---------------------------------------------------------------------------------------------------

$ExplicitHome = [bool]$VeosHome
if (-not $VeosHome) { $VeosHome = Resolve-VeosHome }
$Home_ = [IO.Path]::GetFullPath($VeosHome)
$LegacyHome = [IO.Path]::GetFullPath((Get-VeosHomes)[1])
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
$AppStamp = Join-Path $State 'app.version'
New-Item -ItemType Directory -Force -Path $Dl, $State | Out-Null

function Log([string]$m) { try { Add-Content -Path $LogFile -Value ("{0} {1}" -f (Get-Date -Format s), $m) } catch {} }
function Step([string]$name, [string]$label) {
  $script:Step = $name; $script:N++
  $line = "[{0}/{1}] {2}" -f $script:N, $TOTAL, $label
  Write-Host $line; Log $line
}
function Info([string]$m) { Write-Host "      $m"; Log "      $m" }
function MB([long]$b) { '{0:N0} MB' -f ($b / 1MB) }

# ---- downloads: curl.exe (in Windows since 10 1803; Schannel, so it trusts the Windows certificate store) with resume
# (-C - on <out>.part, kept across tries and runs), a 20 s connect timeout and a stall timeout (under 20 KB/s for 60 s).
$Curl = if ($env:SystemRoot) { Join-Path $env:SystemRoot 'System32\curl.exe' } else { '' }
if (-not ($Curl -and (Test-Path -LiteralPath $Curl))) { $Curl = '' }
$TlsHint = 'The secure connection was blocked or re-signed (a certificate problem). The usual cause is antivirus HTTPS / web scanning (Quick Heal, Kaspersky, ESET, Avast web shield) or an office proxy: pause the web protection or use another network (a phone hotspot), then run setup again; it resumes.'
$ProxyHint = "Couldn't get through this network's proxy. On an office network, use another network (a phone hotspot), then run setup again; it resumes."
$script:NetHint = ''
$script:RetryWait = 5
# 'tls' / 'proxy' / '' from curl's exit code or an error text
function Get-NetProblem([int]$code, [string]$text) {
  if (@(35, 51, 53, 54, 58, 59, 60, 77, 80, 83, 90, 91) -contains $code -or $text -match 'SSL|TLS|certificate|trust relationship|secure channel') { return 'tls' }
  if (@(5, 97) -contains $code -or $text -match 'proxy') { return 'proxy' }
  return ''
}
function Fetch([string]$url, [string]$part) {
  if ($Curl) {
    $errFile = "$part.err"
    & $Curl -fL -sS --connect-timeout 20 --speed-limit 20000 --speed-time 60 -C - --stderr $errFile -o $part $url
    $code = $LASTEXITCODE; $global:LASTEXITCODE = 0
    $err = if (Test-Path -LiteralPath $errFile) { @("$(Get-Content -LiteralPath $errFile -Raw)".Trim() -split '\r?\n')[0] } else { '' }
    Remove-Item -LiteralPath $errFile -Force -ErrorAction SilentlyContinue
    if ($code -eq 0) { return }
    if (@(33, 36) -contains $code) { Remove-Item -LiteralPath $part -Force -ErrorAction SilentlyContinue }  # can't resume: restart
    throw (New-Object System.Exception("curl exit ${code}: $err", (New-Object System.Exception([string]$code))))
  }
  Invoke-WebRequest -Uri $url -OutFile $part -UseBasicParsing -TimeoutSec 60  # no curl.exe: no resume
}
# Download <urls> (the first, then each mirror) to <out>; with a sha256 every copy must match it. <out> appears only
# when complete and verified; a partial download stays in <out>.part and the next try (or the next run) resumes it.
function Download([string[]]$urls, [string]$out, [string]$sha = '') {
  $dir = Split-Path $out -Parent; New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $part = "$out.part"; $last = ''; $problem = ''
  for ($i = 1; $i -le 3; $i++) {
    foreach ($url in $urls) {
      try {
        Fetch $url $part
        if ($sha) {
          $got = (Get-FileHash -Algorithm SHA256 -Path $part).Hash.ToLower()
          if ($got -ne $sha.ToLower()) { Remove-Item -LiteralPath $part -Force; throw "sha256 mismatch for $(Split-Path $out -Leaf): expected $sha got $got" }
        }
        Move-Item -LiteralPath $part $out -Force
        Info ("downloaded {0} ({1})" -f (Split-Path $out -Leaf), (MB (Get-Item -LiteralPath $out).Length))
        return
      } catch {
        $last = $_.Exception.Message
        $code = 0; if ($_.Exception.InnerException) { [void][int]::TryParse($_.Exception.InnerException.Message, [ref]$code) }
        $p = Get-NetProblem $code $last; if ($p) { $problem = $p }
        Log "download attempt $i failed ($url): $last"
      }
    }
    if ($i -lt 3) { Info "network hiccup, retrying ($i/3)..."; Start-Sleep -Seconds ($script:RetryWait * $i) }
  }
  if ($problem -eq 'tls') { $script:NetHint = $TlsHint } elseif ($problem -eq 'proxy') { $script:NetHint = $ProxyHint }
  throw "download failed after 3 tries: $($urls[0]) ($last)"
}
# uv, curl and Python don't read the Windows (WinINET) proxy setting: hand it to them as HTTPS_PROXY when one is set
function Set-SystemProxy {
  if ($env:HTTPS_PROXY -or $env:https_proxy) { return }
  try {
    $u = [Uri]'https://github.com'; $p = [Net.WebRequest]::GetSystemWebProxy().GetProxy($u)
    if ($p -and $p.Host -ne $u.Host) { $env:HTTPS_PROXY = $p.AbsoluteUri; $env:HTTP_PROXY = $p.AbsoluteUri; Log "using the system proxy $($p.Authority)" }
  } catch {}
}
# keep the PC awake while the installer runs (ES_CONTINUOUS | ES_SYSTEM_REQUIRED; Windows drops it when the process ends)
function Set-StayAwake([bool]$on) {
  if (-not $on -and -not ('Veos.Power' -as [type])) { return }
  try {
    if (-not ('Veos.Power' -as [type])) {
      Add-Type -Namespace Veos -Name Power -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint esFlags);' -ErrorAction Stop
    }
    [void][Veos.Power]::SetThreadExecutionState($(if ($on) { [uint32]2147483649 } else { [uint32]2147483648 }))
  } catch {}
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
# `veos` in any new PowerShell / cmd window: a stable wrapper in VEOS_HOME\bin (the plugin folder moves with every
# update, VEOS_HOME doesn't) and that folder on the USER Path (HKCU, no admin). Idempotent: never added twice.
function Install-VeosWrapper([string]$h) {
  $bin = Join-Path $h 'bin'; New-Item -ItemType Directory -Force -Path $bin | Out-Null
  $src = @((Join-Path $PSScriptRoot '..\bin\veos.cmd'), (Join-Path $h 'app\plugin\bin\veos.cmd')) | Where-Object { Test-Path $_ } | Select-Object -First 1
  if ($src) {
    $txt = [IO.File]::ReadAllText((Resolve-Path $src).Path)
    # the installed folder replaces the default-home lookup (and the lookup itself is dropped)
    $txt = $txt.Replace('if "%H%"=="" call :defaulthome', ('if "%H%"=="" set "H={0}"' -f $h))
    $txt = [regex]::Replace($txt, '(?s)(\r?\n)rem Default VEOS_HOME.*$', '$1')
  } else {
    $txt = "@echo off`r`nsetlocal`r`nset `"H=%VEOS_HOME%`"`r`nif `"%H%`"==`"`" set `"H=$h`"`r`n" +
           "set `"VEOS_HOME=%H%`"`r`nset `"PLAYWRIGHT_BROWSERS_PATH=%H%\browsers`"`r`nset `"HF_HOME=%H%\models\hf`"`r`n" +
           "set `"TORCH_HOME=%H%\models\torch`"`r`nif not exist `"%H%\tmp\`" mkdir `"%H%\tmp`" >nul 2>&1`r`n" +
           "set `"TMP=%H%\tmp`"`r`nset `"TEMP=%H%\tmp`"`r`n" +
           "if exist `"%H%\app`" set `"VEOS_APP=%H%\app`"`r`nset `"PYTHONIOENCODING=utf-8`"`r`nset `"PYTHONUTF8=1`"`r`n" +
           "set `"PATH=%H%\tools\ffmpeg\bin;%PATH%`"`r`n`"%H%\venv\Scripts\python.exe`" -m veos %*`r`nexit /b %ERRORLEVEL%`r`n"
  }
  [IO.File]::WriteAllText((Join-Path $bin 'veos.cmd'), $txt, (New-Object System.Text.UTF8Encoding($false)))
  return $bin
}
function Add-UserPath([string]$dir, [string]$keyName = 'Environment') {
  $key = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey($keyName)
  try {
    $raw = [string]$key.GetValue('Path', '', [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
    $want = $dir.TrimEnd('\').ToLowerInvariant()
    $parts = @($raw -split ';' | Where-Object { $_.Trim() -ne '' })
    foreach ($p in $parts) { if ([Environment]::ExpandEnvironmentVariables($p).Trim().TrimEnd('\').ToLowerInvariant() -eq $want) { return $false } }
    $key.SetValue('Path', ((@($parts) + $dir) -join ';'), [Microsoft.Win32.RegistryValueKind]::ExpandString)
  } finally { $key.Close() }
  # tell Explorer and new terminals that the environment changed (SetEnvironmentVariable broadcasts WM_SETTINGCHANGE)
  if ($keyName -eq 'Environment') { try { [Environment]::SetEnvironmentVariable('VEOS_PATH_REFRESH', $null, 'User') } catch {} }
  return $true
}
function Remove-UserPath([string]$dir, [string]$keyName = 'Environment') {
  $key = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey($keyName)
  try {
    $raw = [string]$key.GetValue('Path', '', [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
    $drop = $dir.TrimEnd('\').ToLowerInvariant()
    $parts = @($raw -split ';' | Where-Object { $_.Trim() -ne '' })
    $keep = @($parts | Where-Object { [Environment]::ExpandEnvironmentVariables($_).Trim().TrimEnd('\').ToLowerInvariant() -ne $drop })
    if ($keep.Count -eq $parts.Count) { return $false }
    $key.SetValue('Path', ($keep -join ';'), [Microsoft.Win32.RegistryValueKind]::ExpandString)
  } finally { $key.Close() }
  if ($keyName -eq 'Environment') { try { [Environment]::SetEnvironmentVariable('VEOS_PATH_REFRESH', $null, 'User') } catch {} }
  return $true
}
# The app zip that matches THIS plugin's version: setup/release.json (written by tools/make_dist.py, with the zip's
# sha256), else the release asset named after plugin.json's version (a local build without release.json; no sha).
function Get-AppRelease {
  $rj = Join-Path $PSScriptRoot 'release.json'
  if (Test-Path -LiteralPath $rj) {
    $r = Get-Content -LiteralPath $rj -Raw | ConvertFrom-Json
    return @{ version = [string]$r.version; urls = @($r.app_urls); sha = [string]$r.app_sha256 }
  }
  $p = Get-Content -LiteralPath (Join-Path $PSScriptRoot '..\.claude-plugin\plugin.json') -Raw | ConvertFrom-Json
  $r = if ($Repo) { $Repo } else { [string]$p.repository }
  if ($r -notmatch '^https?://') { $r = "https://github.com/$r" }
  $r = $r.TrimEnd('/'); if ($r.EndsWith('.git')) { $r = $r.Substring(0, $r.Length - 4) }
  $v = [string]$p.version
  return @{ version = $v; urls = @("$r/releases/download/v$v/vibe-editing-os-app-$v.zip"); sha = '' }
}
# Activate VEOS_LICENCE_KEY with the engine: $null when activated, else the engine's error {code, message, hint}.
function Invoke-Licence {
  $lic = & $VenvPy -m veos licence activate --key $env:VEOS_LICENCE_KEY
  $global:LASTEXITCODE = 0
  $lj = $null; try { $lj = (@($lic) | Select-Object -Last 1) | ConvertFrom-Json } catch {}
  if ($lj -and $lj.ok) { Info $lj.message; return $null }
  if ($lj -and $lj.error) { return $lj.error }
  return @{ code = 'UNEXPECTED'; message = "licence activation gave no answer: $lic"; hint = 'Re-run setup.' }
}
function Finish([bool]$ok, [hashtable]$extra) {
  Set-StayAwake $false
  $o = [ordered]@{ ok = $ok; home = $Home_; seconds = [int]((Get-Date) - $T0).TotalSeconds; log = $LogFile }
  foreach ($k in $extra.Keys) { $o[$k] = $extra[$k] }
  Write-Output ($o | ConvertTo-Json -Compress -Depth 6)
  if ($ok) { exit 0 } else { exit 1 }
}

Set-VeosEnv $Home_ | Out-Null

$hint = @{
  home = 'Check that the folder is writable and the disk has about 6 GB free.'
  app = "Couldn't download the app. Check the internet connection (on Jio, try another network or a phone hotspot) and run setup again; it resumes."
  uv = 'Check your internet connection and re-run; the installer resumes where it stopped.'
  python = 'Check your internet connection and re-run. If the error mentions a certificate, antivirus HTTPS scanning or an office proxy is the likely cause.'
  engine = 'Re-run the installer (it resumes). If the error mentions a certificate, antivirus HTTPS scanning or an office proxy is the likely cause; otherwise send the last lines of install.log.'
  ffmpeg = 'Check your internet connection and re-run (the download is checksum-verified).'
  browser = 'Check your internet connection and re-run. If the error mentions a certificate, antivirus HTTPS scanning or an office proxy is the likely cause.'
  models = 'Check your internet connection and re-run; finished and partial downloads are kept. If the error mentions a certificate, antivirus HTTPS scanning or an office proxy is the likely cause.'
  playbooks = 'Check that VEOS_HOME is writable.'
  doctor = 'Run `veos doctor` and follow the hint on the failing check.'
}

try {
  # ---- 1 home: one installer at a time, then platform + disk checks, all before any download ------------------------
  $script:LockStream = Lock-Install (Join-Path $State 'install.lock')
  if (-not $script:LockStream) {
    $at = Get-RunningStep $LogFile
    $msg = 'Another Vibe Editing OS install is already running' + $(if ($at) { " (now at step $at)" } else { '' }) + '.'
    Write-Host $msg
    Finish $false @{ step = 'busy'; running = $true; error = $msg; hint = 'Let it finish (its progress is in install.log); run setup again only if it stops.' }
  }
  Step 'home' "Preparing $Home_"
  Set-StayAwake $true
  Set-SystemProxy
  $plan = Get-PlatformPlan (Get-MachineArch) ([Environment]::OSVersion.Version.Build)
  if (-not $plan.ok) {
    Write-Host $plan.msg; Log $plan.msg
    Finish $false @{ step = 'platform'; error = $plan.msg; hint = 'Nothing was downloaded or changed.' }
  }
  if ($plan.arm) { Info 'Windows on ARM: installing the x64 versions (they run under Windows 11 built-in emulation)' }
  $needGB = if (Test-Path $VenvPy) { 2 } else { 6 }  # first install peaks at ~5-6 GB (downloads + uv cache); a resume needs less
  $freeGB = Get-FreeGB $Home_
  if (($null -ne $freeGB) -and ($freeGB -lt $needGB)) {
    $msg = "Not enough free disk space: setup needs about $needGB GB free on $([IO.Path]::GetPathRoot($Home_)) and there is $freeGB GB."
    Write-Host $msg; Log $msg
    Finish $false @{ step = 'disk'; error = $msg; hint = 'Free up some space (empty the Recycle Bin, delete big downloads), then run setup again.' }
  }
  if ((-not $ExplicitHome) -and ($Home_ -eq $LegacyHome)) { Info 'keeping your existing install in this folder (Vibe Editing OS 0.6.0 and earlier)' }
  foreach ($r in (Find-PackageRedirect)) {
    Info "an earlier install from inside the Claude app was redirected by Windows to $r; this install doesn't use it (you can delete that folder)"
  }
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
    Set-Content -Path $AppStamp -Value 'local source' -Encoding ascii
  } else {
    $rel = Get-AppRelease
    $complete = @($appDirs | Where-Object { -not (Test-Path (Join-Path $App $_)) }).Count -eq 0
    $have = if (Test-Path $AppStamp) { (Get-Content $AppStamp -Raw).Trim() } else { '' }
    if ($complete -and $have -eq $rel.version -and -not $Update) { Info "app $($rel.version) already in place" } else {
      Info "downloading the app (version $($rel.version))"
      $z = Join-Path $Dl "vibe-editing-os-app-$($rel.version).zip"; $x = Join-Path $Dl 'app-x'
      Download $rel.urls $z $rel.sha
      Unzip $z $x
      $top = Get-ChildItem $x | Select-Object -First 1
      if (Test-Path $App) { Remove-Item $App -Recurse -Force }
      New-Item -ItemType Directory -Force -Path $App | Out-Null
      foreach ($d in $appDirs) { Copy-Item -Recurse -Force (Join-Path $top.FullName $d) (Join-Path $App $d) }
      Remove-Item $z, $x -Recurse -Force
      Set-Content -Path $AppStamp -Value $rel.version -Encoding ascii
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
    $asset = 'uv-x86_64-pc-windows-msvc.zip'  # x64 on every PC (ARM PCs run it under emulation, like the x64 Python)
    $base = "https://github.com/astral-sh/uv/releases/download/$UV_VERSION/$asset"
    $z = Join-Path $Dl $asset
    $shaFile = Join-Path $Dl "$asset.sha256"
    if (Test-Path $shaFile) { Remove-Item $shaFile -Force }
    Download "$base.sha256" $shaFile
    $sha = ((Get-Content -LiteralPath $shaFile -Raw).Trim() -split '\s+')[0]
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
  # a working venv needs nothing here (an update never touches the Python folder or its links)
  $pyOk = $false
  # an x64 Python 3.12 (win-amd64: the platform every engine wheel exists for, also on ARM PCs)
  if (Test-Path $VenvPy) { try { $pyOk = ((& $VenvPy -c "import sys, sysconfig; print(sys.version_info[:2] == (3, 12) and sysconfig.get_platform() == 'win-amd64')") -eq 'True') } catch {}; $global:LASTEXITCODE = 0 }
  if ($pyOk) { Info 'Python 3.12 already installed' } else {
    if (Test-Path $Venv) { Remove-Item $Venv -Recurse -Force }  # a broken or ARM venv is rebuilt
    Retry { Run $Uv @('python', 'install', $plan.python) } 'python download'
  }
  if (-not (Test-Path $VenvPy)) { Run $Uv @('venv', $Venv, '--python', $plan.python) } else { Info 'venv already exists' }

  # ---- 5 engine ------------------------------------------------------------------------------------------------
  Step 'engine' 'Installing the veos engine and its packages (~700 MB)'
  $stamp = Join-Path $State 'engine.sha'
  $have = if (Test-Path $stamp) { (Get-Content $stamp -Raw).Trim() } else { '' }
  # Always sync to EXACTLY the locked set (removes extras, restores changed versions); a no-op when already matching.
  $req = Join-Path $Dl 'requirements.txt'
  Run $Uv @('export', '--project', (Join-Path $App 'engine'), '--frozen', '--no-dev', '--no-emit-project', '--no-hashes', '-o', $req, '-q')
  # --no-build: binary wheels only, so nothing is ever compiled (no compiler needed; a missing wheel fails plainly)
  Retry { Run $Uv @('pip', 'sync', '--no-build', '--python', $VenvPy, $req) } 'package sync'
  # editable: the engine locates renderer/, assets/, playbooks/ relative to app/engine/src, so it must run from app/
  Retry { Run $Uv @('pip', 'install', '--python', $VenvPy, '--no-deps', '-e', (Join-Path $App 'engine')) } 'engine install'
  Remove-Item $req -Force -ErrorAction SilentlyContinue
  Set-Content -Path $stamp -Value $after -Encoding ascii

  # licence: activate as soon as the engine exists, before the big downloads (key from the setup skill, env only). A
  # wrong key stops here; an unreachable licence server doesn't: the install goes on and tries again at the end.
  $licPending = $false
  if ($env:VEOS_LICENCE_KEY) {
    $script:Step = 'licence'
    Info 'activating your licence'
    $le = Invoke-Licence
    if ($le -and $le.code -eq 'LICENCE_OFFLINE') {
      $licPending = $true; Log 'licence server unreachable; activation retried at the end'
      Info "couldn't reach the licence server; carrying on with the install and trying again at the end"
    } elseif ($le) {
      Log "licence activation failed: $($le.code)"
      Write-Host "FAILED at step 'licence': $($le.message)"
      Finish $false @{ step = 'licence'; licence_error = $le.code; error = $le.message; hint = $le.hint }
    }
    $script:Step = 'engine'
  }

  # ---- 6 ffmpeg ------------------------------------------------------------------------------------------------
  Step 'ffmpeg' "ffmpeg $FFMPEG_VERSION (~110 MB, checksum-verified)"
  $ffDir = Join-Path $Tools 'ffmpeg'; $ffVer = Join-Path $ffDir 'VERSION'
  if ((Test-Path (Join-Path $ffDir 'bin\ffmpeg.exe')) -and (Test-Path (Join-Path $ffDir 'bin\ffprobe.exe'))) {
    Info 'already installed'
  } else {
    $z = Join-Path $Dl "$FFMPEG_NAME.zip"
    Download $FFMPEG_URLS $z $FFMPEG_SHA
    $x = Join-Path $Dl 'ffmpeg-x'; Unzip $z $x
    $inner = Get-ChildItem $x | Select-Object -First 1
    if (Test-Path $ffDir) { Remove-Item $ffDir -Recurse -Force }
    Move-Item $inner.FullName $ffDir
    Remove-Item (Join-Path $ffDir 'bin\ffplay.exe'), (Join-Path $ffDir 'doc') -Recurse -Force -ErrorAction SilentlyContinue  # not used (~100 MB)
    Set-Content -Path $ffVer -Value $FFMPEG_NAME -Encoding ascii
    Remove-Item $z, $x -Recurse -Force -ErrorAction SilentlyContinue
  }

  # ---- 7 chromium ----------------------------------------------------------------------------------------------
  Step 'browser' 'Chromium for rendering (Playwright, ~350 MB)'
  Retry { Run $VenvPy @('-m', 'playwright', 'install', 'chromium') } 'chromium download'

  # ---- 8 models ------------------------------------------------------------------------------------------------
  Step 'models' 'AI models: background matte (~14 MB), face detector (~1 MB), speaker labels (~34 MB), speech-to-text whisper turbo (~1.6 GB)'
  if ($SkipModels) { Info 'skipped (-SkipModels)' } else {
    $rvm = Join-Path $Home_ 'models\rvm\rvm_mobilenetv3_fp32.onnx'
    if (-not (Test-Path $rvm)) { Download $RVM_URL $rvm } else { Info 'RVM already present' }
    $face = Join-Path $Home_ 'models\mediapipe\blaze_face_short_range.tflite'
    if (-not (Test-Path $face)) { Download $FACE_URL $face } else { Info 'face model already present' }
    $yn = Join-Path $Home_ 'models\yunet\face_detection_yunet_2023mar.onnx'
    if ((Test-Path $yn) -and ((Get-FileHash -Algorithm SHA256 -Path $yn).Hash.ToLower() -ne $YUNET_SHA)) { Remove-Item $yn -Force }
    if (-not (Test-Path $yn)) { Download $YUNET_URL $yn $YUNET_SHA } else { Info 'YuNet face model already present' }
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
    if (-not (Test-Path $emb)) { Download $SPKEMB_URL $emb $SPKEMB_SHA } else { Info 'speaker embedding model already present' }
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
  Step 'doctor' 'Putting veos on your PATH, then checking everything with veos doctor'
  $bin = Install-VeosWrapper $Home_
  if (Add-UserPath $bin) { Info "added $bin to your user PATH (new terminals know 'veos')" } else { Info "veos already on your user PATH ($bin)" }
  if ((-not $ExplicitHome) -and ($Home_ -ne $LegacyHome) -and (Remove-UserPath (Join-Path $LegacyHome 'bin'))) {
    Info "removed the old folder's veos ($LegacyHome\bin) from your user PATH"
  }
  $env:PATH = $bin + ';' + (Join-Path $Home_ 'tools\ffmpeg\bin') + ';' + $env:PATH
  $licExtra = @{}
  if ($licPending) {
    Info 'activating your licence (second try)'
    $le = Invoke-Licence
    if ($le) {
      $lm = if ($le.code -eq 'LICENCE_OFFLINE') { "Everything is installed, but the licence server couldn't be reached, so the licence isn't activated yet. Check the internet connection, then run /vibe-editing-os:setup licence." } else { $le.message }
      Info $lm; Log "licence still not activated: $($le.code)"
      $licExtra = @{ licence_pending = $true; licence_error = $le.code; licence_message = $lm }
    }
  }
  $doc = & $VenvPy -m veos doctor
  $global:LASTEXITCODE = 0
  $ready = $false; $problems = @()
  try { $j = ($doc | Out-String) | ConvertFrom-Json; $ready = [bool]$j.ready; $problems = @($j.problems) } catch { $problems = @("doctor output unreadable: $doc") }
  Info $(if ($ready) { 'doctor: ready' } else { 'doctor: problems found' })
  Remove-Item $Dl -Recurse -Force -ErrorAction SilentlyContinue
  Remove-Item (Join-Path $Home_ 'cache') -Recurse -Force -ErrorAction SilentlyContinue  # uv download cache (~800 MB), not needed after install
  Remove-Item (Join-Path $Home_ 'tmp\*') -Recurse -Force -ErrorAction SilentlyContinue

  $size = (Get-ChildItem $Home_ -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  Finish $true (@{ doctor_ready = $ready; problems = $problems; size_mb = [int]($size / 1MB); app = $App; venv = $Venv } + $licExtra)
} catch {
  $msg = $_.Exception.Message
  Log "FAILED at $script:Step : $msg"
  Write-Host "FAILED at step '$script:Step': $msg"
  $h = if ($script:NetHint) { $script:NetHint } else { $hint[$script:Step] }
  Finish $false @{ step = $script:Step; error = $msg; hint = $h }
}
