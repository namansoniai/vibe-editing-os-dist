#!/usr/bin/env bash
# Vibe Editing OS - one-time installer (macOS arm64 first, Linux best-effort). No sudo, nothing outside VEOS_HOME.
# Idempotent + resumable. Re-run any time; --update refreshes the app.
#
#   --home DIR         VEOS_HOME (default ~/Library/Application Support/VibeEditingOS)
#   --app-source DIR   copy the app from a local checkout instead of the app zip (testing). env VEOS_APP_SOURCE
#   --repo URL         override the GitHub repo of the app zip (default: plugin.json "repository"). env VEOS_REPO
#   --update           download the app again and resync the engine
#   The app is always the zip of THIS plugin's version (setup/release.json from the dist build, sha256-pinned), so the
#   engine and the skills never drift apart. No git and no compiler anywhere (no developer-tools pop-up on a Mac).
#   --skip-models      skip the ~1.7 GB model downloads
#   env VEOS_LICENCE_KEY  activate this licence key right after the engine step (before the big downloads); a rejected
#                         key stops the install with step "licence" and licence_error = the engine's code. An unreachable
#                         licence server (LICENCE_OFFLINE) never stops it: the downloads go on, the activation is tried
#                         again at the end, and if it still fails the result is ok with licence_pending = true.
# Output: one progress line per step, final line JSON {"ok":true|false,...}. Log: VEOS_HOME/install.log
set -u

UV_VERSION="0.12.23"
RVM_URL="https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx"
YUNET_URL="https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"
YUNET_SHA="8f2383e4dd3cfbb4553ea8718107fc0423210dc964f9f4280604804ed2552fa4"
FACE_URL="https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite"
# speaker labels for multi-speaker reels (no account/token): pyannote segmentation-3.0 (MIT) + CAM++ (Apache-2.0)
SPKSEG_URL="https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-segmentation-models/sherpa-onnx-pyannote-segmentation-3-0.tar.bz2"
SPKSEG_SHA="24615ee884c897d9d2ba09bb4d30da6bb1b15e685065962db5b02e76e4996488"
SPKEMB_URL="https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/3dspeaker_speech_campplus_sv_en_voxceleb_16k.onnx"
SPKEMB_SHA="357a834f702b80161e5b981182c038e18553c1f2ca752ed6cec2052365d4129b"
WHISPER_REPO="mobiuslabsgmbh/faster-whisper-large-v3-turbo"
TOTAL=10

OS="$(uname -s)"; ARCH="$(uname -m)"
# a shell running under Rosetta reports x86_64 on Apple Silicon; we still want the native arm64 tools
if [ "$OS" = Darwin ] && [ "$ARCH" = x86_64 ] && [ "$(sysctl -n hw.optional.arm64 2>/dev/null || echo 0)" = 1 ]; then ARCH=arm64; fi
# DRY_RUN=1 [DRY_PLATFORM=Darwin-arm64]: print + HEAD-check every URL for that platform, install nothing
DRY_RUN="${DRY_RUN:-0}"
if [ -n "${DRY_PLATFORM:-}" ]; then OS="${DRY_PLATFORM%%-*}"; ARCH="${DRY_PLATFORM#*-}"; fi
SETUP_DIR="$(cd "$(dirname "$0")" && pwd)"
case "$OS" in
  Darwin) DEFAULT_HOME="$HOME/Library/Application Support/VibeEditingOS" ;;
  *) DEFAULT_HOME="${XDG_DATA_HOME:-$HOME/.local/share}/VibeEditingOS" ;;
esac
HOME_DIR="${VEOS_HOME:-$DEFAULT_HOME}"
APP_SOURCE="${VEOS_APP_SOURCE:-}"
REPO="${VEOS_REPO:-}"
UPDATE=0; SKIP_MODELS=0
while [ $# -gt 0 ]; do
  case "$1" in
    --home) HOME_DIR="$2"; shift 2 ;;
    --app-source) APP_SOURCE="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --update) UPDATE=1; shift ;;
    --skip-models) SKIP_MODELS=1; shift ;;
    *) echo "unknown option $1" >&2; exit 2 ;;
  esac
done

T0=$(date +%s)
STEP=start; N=0
mkdir -p "$HOME_DIR"
HOME_DIR="$(cd "$HOME_DIR" && pwd)"
LOG="$HOME_DIR/install.log"
DL="$HOME_DIR/scratch/downloads"; APP="$HOME_DIR/app"; TOOLS="$HOME_DIR/tools"; VENV="$HOME_DIR/venv"
VENVPY="$VENV/bin/python"; UV="$TOOLS/uv/uv"; STATE="$HOME_DIR/state"
mkdir -p "$DL" "$STATE" "$TOOLS"

log() { echo "$(date +%FT%T) $*" >> "$LOG"; }
step() { STEP="$1"; N=$((N+1)); echo "[$N/$TOTAL] $2"; log "[$N/$TOTAL] $2"; }
info() { echo "      $*"; log "      $*"; }
size_of() { du -sm "$1" 2>/dev/null | cut -f1; }
json_escape() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g' | tr '\n\r\t' '   '; }

hint_for() {
  case "$1" in
    app) echo "Couldn't download the app. Check the internet connection (on Jio, try another network or a phone hotspot) and run setup again; it resumes." ;;
    uv|python|ffmpeg|browser|models|engine) echo "Check your internet connection and re-run; the installer resumes where it stopped. If the error mentions a certificate, antivirus HTTPS scanning or an office proxy is the likely cause." ;;
    doctor) echo "Run veos doctor and follow the hint on the failing check." ;;
    *) echo "Re-run the installer. If it persists, send the last lines of install.log." ;;
  esac
}
fail() {
  local msg="$1"
  log "FAILED at $STEP: $msg"; echo "FAILED at step '$STEP': $msg"
  printf '{"ok":false,"step":"%s","error":"%s","hint":"%s","home":"%s","seconds":%d,"log":"%s"}\n' \
    "$STEP" "$(json_escape "$msg")" "$(json_escape "${NET_HINT:-$(hint_for "$STEP")}")" "$(json_escape "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")"
  exit 1
}
stop() { # stop <step> <message> <hint>: a plain answer (not a crash), then the JSON line
  STEP="$1"; log "$2"; echo "$2"
  printf '{"ok":false,"step":"%s","error":"%s","hint":"%s","home":"%s","seconds":%d,"log":"%s"}\n' \
    "$1" "$(json_escape "$2")" "$(json_escape "$3")" "$(json_escape "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")"
  exit 1
}
trap 'fail "unexpected error (line $LINENO)"' ERR
set -e

# ---- BEGIN preflight: checks before any download (engine/tests/test_install_scripts.py runs this block on its own)
# platform_problem <os> <arch> <macOS version>: prints why this computer can't run the engine, nothing when it can.
# The engine's wheels need Apple Silicon (onnxruntime and mediapipe have no Intel build) and macOS 14 (onnxruntime).
platform_problem() {
  case "$1" in
    Darwin)
      local major="${3%%.*}"
      case "$major" in ''|*[!0-9]*) major=0 ;; esac
      if [ "$2" != arm64 ] || [ "$major" -lt 14 ]; then
        echo "This Mac isn't supported yet: Vibe Editing OS needs an Apple Silicon Mac (M1 or later) on macOS 14 or newer."
      fi ;;
  esac
}
# One installer at a time: a lock folder holding the installer's PID. A lock whose PID is gone (crashed, closed) is stale.
take_lock() { # take_lock <dir> -> 0 = ours, 1 = another installer is running
  if mkdir "$1" 2>/dev/null; then echo $$ > "$1/pid"; return 0; fi
  local other; other="$(cat "$1/pid" 2>/dev/null || true)"
  if [ -n "$other" ] && [ "$other" != $$ ] && kill -0 "$other" 2>/dev/null; then return 1; fi
  rm -rf "$1"; mkdir "$1" 2>/dev/null || return 1; echo $$ > "$1/pid"; return 0
}
running_step() { grep -o '\[[0-9]*/[0-9]*\]' "$1" 2>/dev/null | tail -n 1 | tr -d '[]' || true; }
# ---- END preflight

retry() { # retry <what> cmd...
  local what="$1"; shift; local i
  for i in 1 2 3; do
    if "$@"; then return 0; fi
    log "$what attempt $i failed"
    [ "$i" -lt 3 ] && { info "$what failed, retrying ($i/3)..."; sleep $((3*i)); }
  done
  return 1
}
sha256_of() { if command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | cut -d' ' -f1; else sha256sum "$1" | cut -d' ' -f1; fi; }
TLS_HINT="The secure connection was blocked or re-signed (a certificate problem). The usual cause is antivirus HTTPS / web scanning or an office proxy: pause the web protection or use another network (a phone hotspot), then run setup again; it resumes."
PROXY_HINT="Couldn't get through this network's proxy. On an office network, use another network (a phone hotspot), then run setup again; it resumes."
NET_HINT=""; RETRY_WAIT="${RETRY_WAIT:-5}"
net_problem() { # net_problem <curl exit code> -> tls / proxy / nothing
  case "$1" in 35|51|53|54|58|59|60|77|80|83|90|91) echo tls ;; 5|97) echo proxy ;; esac
}
# download "<url> [mirror ...]" <out> [sha256]: the first URL, then each mirror; every copy must match the sha. <out>
# appears only when complete and verified; a partial download stays in <out>.part and the next try (or run) resumes it.
# 20 s connect timeout; a stall (under 20 KB/s for 60 s) counts as a failed try.
download() {
  local urls="$1" out="$2" sha="${3:-}" part="$2.part" i u rc got problem=""
  mkdir -p "$(dirname "$out")"
  for i in 1 2 3; do
    for u in $urls; do
      rc=0
      curl -fL -sS --connect-timeout 20 --speed-limit 20000 --speed-time 60 -C - -o "$part" "$u" 2>>"$LOG" || rc=$?
      if [ "$rc" = 0 ]; then
        got="$(sha256_of "$part")"
        if [ -n "$sha" ] && [ "$got" != "$sha" ]; then rm -f "$part"; log "sha256 mismatch for $(basename "$out") from $u: got $got"; continue; fi
        mv -f "$part" "$out"
        info "downloaded $(basename "$out") ($(( $(wc -c < "$out") / 1048576 )) MB)"
        return 0
      fi
      case "$rc" in 33|36) rm -f "$part" ;; esac   # the server can't resume: start over
      [ -n "$(net_problem "$rc")" ] && problem="$(net_problem "$rc")"
      log "download attempt $i failed: $u (curl exit $rc)"
    done
    [ "$i" -lt 3 ] && { info "network hiccup, retrying ($i/3)..."; sleep $((RETRY_WAIT*i)); }
  done
  case "$problem" in tls) NET_HINT="$TLS_HINT" ;; proxy) NET_HINT="$PROXY_HINT" ;; esac
  fail "download failed after 3 tries: ${urls%% *}"
}

uv_target() {
  case "$OS-$ARCH" in
    Darwin-arm64) echo "aarch64-apple-darwin" ;;
    Darwin-x86_64) echo "x86_64-apple-darwin" ;;
    Linux-x86_64) echo "x86_64-unknown-linux-gnu" ;;
    Linux-aarch64) echo "aarch64-unknown-linux-gnu" ;;
    *) return 1 ;;
  esac
}
# ffmpeg + ffprobe: one stable release, pinned by version + sha256 (martin-riedl.de keeps every release build; static,
# with libx264, aac, libwebp and every built-in filter the engine uses). Never "latest" or a nightly.
FFMPEG_VERSION="9.0.2"
FFMPEG_BASE="https://ffmpeg.martin-riedl.de/download"
ffmpeg_pin() { # ffmpeg_pin <ffmpeg|ffprobe> -> "<url> <sha256>" for this platform
  case "$OS-$ARCH-$1" in
    Darwin-arm64-ffmpeg)   echo "$FFMPEG_BASE/macos/arm64/1789931890_9.0.2/ffmpeg.zip c8ed4c4e6978a03c485edbfe4e0a5dc2380f8a30bba5150531b31b094492d924" ;;
    Darwin-arm64-ffprobe)  echo "$FFMPEG_BASE/macos/arm64/1789931890_9.0.2/ffprobe.zip fcbe839537485eaee7a7a8bc5cbc0f90d53617e80943e8a5b2e31cb851197ea6" ;;
    Linux-x86_64-ffmpeg)   echo "$FFMPEG_BASE/linux/amd64/1789931100_9.0.2/ffmpeg.zip fa8ecf4abbd290d98f7d188b8649cc6b391ae209a98452be955a15aab1909d7f" ;;
    Linux-x86_64-ffprobe)  echo "$FFMPEG_BASE/linux/amd64/1789931100_9.0.2/ffprobe.zip 3f428c49070be3d24ec338602b76d412e401ffcb8a5641ef0e729181a232fc32" ;;
    Linux-aarch64-ffmpeg)  echo "$FFMPEG_BASE/linux/arm64/1789931697_9.0.2/ffmpeg.zip 93a76ae90db5474eecdf951a729857c64f3de23567228d6a7d5e6e8e3cd1021b" ;;
    Linux-aarch64-ffprobe) echo "$FFMPEG_BASE/linux/arm64/1789931697_9.0.2/ffprobe.zip bcbe80fb741c180083327afaf5434812e006b33cacde2016b9aeaf6936128330" ;;
    *) return 1 ;;
  esac
}
UV_BASE="https://github.com/astral-sh/uv/releases/download/$UV_VERSION"
# The app zip that matches THIS plugin's version: setup/release.json (written by tools/make_dist.py, with the zip's
# sha256), else the release asset named after plugin.json's version (a local build without release.json; no sha).
# Sets APP_VERSION, APP_URLS (space-separated: first, then mirrors), APP_SHA.
app_release() {
  local rj="$SETUP_DIR/release.json" pj="$SETUP_DIR/../.claude-plugin/plugin.json" r
  if [ -f "$rj" ]; then
    APP_VERSION="$(sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$rj" | head -1)"
    APP_URLS="$(grep -o '"https://[^"]*"' "$rj" | tr -d '"' | tr '\n' ' ')"; APP_URLS="${APP_URLS% }"
    APP_SHA="$(sed -n 's/.*"app_sha256"[[:space:]]*:[[:space:]]*"\([0-9a-f]*\)".*/\1/p' "$rj" | head -1)"
    return 0
  fi
  APP_VERSION="$(sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$pj" | head -1)"
  r="${REPO:-$(sed -n 's/.*"repository"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$pj" | head -1)}"
  case "$r" in http*) ;; *) r="https://github.com/$r" ;; esac
  r="${r%/}"; r="${r%.git}"
  APP_URLS="$r/releases/download/v$APP_VERSION/vibe-editing-os-app-$APP_VERSION.zip"; APP_SHA=""
}

if [ "$DRY_RUN" = 1 ]; then
  bad=0
  check() { code="$(curl -sS -m 30 -L -r 0-0 -o /dev/null -w '%{http_code}' "$1" 2>/dev/null || echo 000)"; echo "$code $1"; case "$code" in 200|206) ;; *) bad=1 ;; esac; }
  echo "DRY RUN for $OS-$ARCH (nothing is installed)"
  UVT="$(uv_target)" || { echo "unsupported platform"; exit 1; }
  check "$UV_BASE/uv-$UVT.tar.gz"; check "$UV_BASE/uv-$UVT.tar.gz.sha256"
  for b in ffmpeg ffprobe; do P="$(ffmpeg_pin $b)" || { echo "no ffmpeg pin for $OS-$ARCH"; exit 1; }; check "${P%% *}"; done
  check "$RVM_URL"; check "$FACE_URL"; check "$YUNET_URL"; check "$SPKSEG_URL"; check "$SPKEMB_URL"
  check "https://huggingface.co/$WHISPER_REPO/resolve/main/config.json"
  app_release; check "${APP_URLS%% *}"
  echo "would run: uv python install 3.12; uv venv; uv export --frozen | uv pip sync --no-build; uv pip install -e app/engine; python -m playwright install chromium; veos doctor"
  exit $bad
fi

# ---- preflight, before any download: one installer at a time, a supported Mac, enough disk
LOCKD="$STATE/install.lock"
if ! take_lock "$LOCKD"; then
  AT="$(running_step "$LOG")"
  stop busy "Another Vibe Editing OS install is already running${AT:+ (now at step $AT)}." \
    "Let it finish (its progress is in install.log); run setup again only if it stops."
fi
trap 'rm -rf "$LOCKD"' EXIT
MACV="$(sw_vers -productVersion 2>/dev/null || echo 0)"
PROBLEM="$(platform_problem "$OS" "$ARCH" "$MACV")"
[ -z "$PROBLEM" ] || stop platform "$PROBLEM" "Nothing was downloaded or changed."
NEED_GB=6; [ -x "$VENVPY" ] && NEED_GB=2   # a first install peaks at ~5-6 GB (downloads + uv cache); a resume needs less
FREE_KB="$(df -Pk "$HOME_DIR" 2>/dev/null | awk 'NR==2 {print $4}')"
case "$FREE_KB" in ''|*[!0-9]*) FREE_KB="" ;; esac
if [ -n "$FREE_KB" ] && [ "$FREE_KB" -lt $((NEED_GB * 1048576)) ]; then
  stop disk "Not enough free disk space: setup needs about $NEED_GB GB free and there is $((FREE_KB / 1048576)) GB." \
    "Free up some space (empty the Trash, delete big downloads), then run setup again."
fi

# keep the Mac awake while the installer runs (caffeinate ends with this script's process)
if [ "$OS" = Darwin ] && command -v caffeinate >/dev/null 2>&1; then caffeinate -i -w $$ >/dev/null 2>&1 & fi

# process-scoped environment only
export VEOS_HOME="$HOME_DIR"
export UV_PYTHON_INSTALL_DIR="$HOME_DIR/python"
export UV_CACHE_DIR="$HOME_DIR/cache/uv"
export UV_PYTHON_PREFERENCE=only-managed
export UV_LINK_MODE=copy
export UV_NO_PROGRESS=1
export UV_HTTP_TIMEOUT=120
export UV_SYSTEM_CERTS=1 NODE_USE_SYSTEM_CA=1   # trust the system certificate store (antivirus / office proxy roots)
export PLAYWRIGHT_BROWSERS_PATH="$HOME_DIR/browsers"
export HF_HOME="$HOME_DIR/models/hf"
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
export PYTHONIOENCODING=utf-8 PYTHONUTF8=1

# ---- 1 home
step home "Preparing $HOME_DIR"
mkdir -p "$HOME_DIR"/{tools,browsers,models/rvm,models/mediapipe,models/yunet,models/hf,playbooks,scratch,cache,sfx}   # sfx = on-demand sound cache (veos sfx fetch); no bulk download

# ---- 2 app
step app "Getting the Vibe Editing OS app (engine, renderer, playbooks, assets)"
APPDIRS="engine renderer playbooks assets"
hash_of() { cat "$APP/engine/pyproject.toml" "$APP/engine/uv.lock" 2>/dev/null | { shasum -a 256 2>/dev/null || sha256sum; } | cut -d' ' -f1; }
if [ -n "$APP_SOURCE" ]; then
  info "copying from local source $APP_SOURCE"
  for d in $APPDIRS; do
    [ -d "$APP_SOURCE/$d" ] || fail "$APP_SOURCE/$d not found"
    mkdir -p "$APP/$d"
    rsync -a --delete --exclude .git --exclude __pycache__ --exclude .pytest_cache --exclude .venv --exclude node_modules \
      --exclude inspiration --exclude '*.mp4' --exclude '*.mov' --exclude '*.mkv' --exclude '*.wav' --exclude '*.m4a' \
      --exclude '*.onnx' --exclude '*.bin' "$APP_SOURCE/$d/" "$APP/$d/"
  done
  echo "local source" > "$STATE/app.version"
else
  app_release
  HAVE_APP="$(cat "$STATE/app.version" 2>/dev/null || true)"; COMPLETE=1
  for d in $APPDIRS; do [ -d "$APP/$d" ] || COMPLETE=0; done
  if [ "$COMPLETE" = 1 ] && [ "$HAVE_APP" = "$APP_VERSION" ] && [ "$UPDATE" = 0 ]; then info "app $APP_VERSION already in place"; else
    info "downloading the app (version $APP_VERSION)"
    Z="$DL/vibe-editing-os-app-$APP_VERSION.zip"
    download "$APP_URLS" "$Z" "$APP_SHA"
    rm -rf "$DL/app-x"; mkdir -p "$DL/app-x"; unzip -q "$Z" -d "$DL/app-x" || fail "could not unpack the app"
    TOP="$(ls -d "$DL"/app-x/*/ | head -1)"
    rm -rf "$APP"; mkdir -p "$APP"
    for d in $APPDIRS; do [ -d "$TOP$d" ] && cp -R "$TOP$d" "$APP/$d"; done
    rm -rf "$Z" "$DL/app-x"
    echo "$APP_VERSION" > "$STATE/app.version"
  fi
fi
for d in $APPDIRS; do [ -d "$APP/$d" ] || fail "app is incomplete: $d missing"; done
AFTER="$(hash_of)"
info "app ready at $APP"

# ---- 3 uv
step uv "uv $UV_VERSION (Python manager)"
if [ -x "$UV" ] && "$UV" --version 2>/dev/null | grep -q "$UV_VERSION"; then info "already installed"; else
  UVT="$(uv_target)" || fail "unsupported platform $OS-$ARCH"
  ASSET="uv-$UVT.tar.gz"; BASE="$UV_BASE/$ASSET"
  rm -f "$DL/$ASSET.sha256"; download "$BASE.sha256" "$DL/$ASSET.sha256"; SHA="$(awk '{print $1}' "$DL/$ASSET.sha256")"
  download "$BASE" "$DL/$ASSET" "$SHA"
  rm -rf "$DL/uv-x"; mkdir -p "$DL/uv-x" "$TOOLS/uv"; tar -xzf "$DL/$ASSET" -C "$DL/uv-x"
  cp "$(dirname "$(find "$DL/uv-x" -name uv -type f | head -1)")"/uv* "$TOOLS/uv/"; chmod +x "$TOOLS/uv/"*
  rm -rf "$DL/${ASSET:?}" "$DL/uv-x"
fi
[ -x "$UV" ] || fail "uv missing after install"

# ---- 4 python + venv
step python "Python 3.12 + virtual environment (~70 MB)"
retry "python download" "$UV" python install 3.12 || fail "uv python install failed"
[ -x "$VENVPY" ] || "$UV" venv "$VENV" --python 3.12

# ---- 5 engine
step engine "Installing the veos engine and its packages (~700 MB)"
# Always sync to EXACTLY the locked set (removes extras, restores changed versions, e.g. a hand-downgraded package);
# uv makes this a no-op when the venv already matches.
"$UV" export --project "$APP/engine" --frozen --no-dev --no-emit-project --no-hashes -o "$DL/requirements.txt" -q
# --no-build: binary wheels only, so nothing is ever compiled (no clang, no developer-tools pop-up on a Mac)
retry "package sync" "$UV" pip sync --no-build --python "$VENVPY" "$DL/requirements.txt" || fail "uv pip sync failed"
# editable: the engine finds renderer/, assets/, playbooks/ relative to app/engine/src
retry "engine install" "$UV" pip install --python "$VENVPY" --no-deps -e "$APP/engine" || fail "engine install failed"
rm -f "$DL/requirements.txt"; echo "$AFTER" > "$STATE/engine.sha"

# licence: activate as soon as the engine exists, before the big downloads (key from the setup skill, env only). A wrong
# key stops here; an unreachable licence server doesn't: the install goes on and tries again at the end.
# activate_licence: sets LIC_CODE ("" = activated) and LIC_JSON (the engine's error fields, for the result line)
activate_licence() {
  local lic
  lic="$("$VENVPY" -m veos licence activate --key "$VEOS_LICENCE_KEY" 2>/dev/null | tail -n 1 || true)"
  if [ "$(printf '%s' "$lic" | "$VENVPY" -c 'import sys,json; print(str(bool(json.load(sys.stdin).get("ok"))).lower())' 2>/dev/null || echo false)" = true ]; then
    LIC_CODE=""; info "$(printf '%s' "$lic" | "$VENVPY" -c 'import sys,json; print(json.load(sys.stdin).get("message",""))' 2>/dev/null || true)"
    return 0
  fi
  LIC_CODE="$(printf '%s' "$lic" | "$VENVPY" -c 'import sys,json; print((json.load(sys.stdin).get("error") or {}).get("code","UNEXPECTED"))' 2>/dev/null || echo UNEXPECTED)"
  LIC_JSON="$(printf '%s' "$lic" | "$VENVPY" -c 'import sys,json; e=json.load(sys.stdin).get("error") or {}; print(json.dumps({"licence_error":e.get("code","UNEXPECTED"),"error":e.get("message","licence activation gave no answer"),"hint":e.get("hint","Re-run setup.")})[1:-1])' 2>/dev/null || echo '"licence_error":"UNEXPECTED","error":"licence activation gave no answer","hint":"Re-run setup."')"
}
LIC_PENDING=0
if [ -n "${VEOS_LICENCE_KEY:-}" ]; then
  STEP=licence
  info "activating your licence"
  activate_licence
  if [ "$LIC_CODE" = LICENCE_OFFLINE ]; then
    LIC_PENDING=1; log "licence server unreachable; activation retried at the end"
    info "couldn't reach the licence server; carrying on with the install and trying again at the end"
  elif [ -n "$LIC_CODE" ]; then
    log "licence activation failed: $LIC_CODE"; echo "FAILED at step 'licence'"
    printf '{"ok":false,"step":"licence",%s,"home":"%s","seconds":%d,"log":"%s"}\n' \
      "$LIC_JSON" "$(json_escape "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")"
    exit 1
  fi
  STEP=engine
fi

# ---- 6 ffmpeg
step ffmpeg "ffmpeg $FFMPEG_VERSION + ffprobe (~55 MB, checksum-verified)"
FF="$TOOLS/ffmpeg/bin"
if [ -x "$FF/ffmpeg" ] && [ -x "$FF/ffprobe" ]; then info "already installed"; else
  mkdir -p "$FF"
  ffmpeg_pin ffmpeg >/dev/null || fail "no ffmpeg build for $OS-$ARCH"
  for b in ffmpeg ffprobe; do
    P="$(ffmpeg_pin $b)"
    download "${P%% *}" "$DL/$b-$FFMPEG_VERSION.zip" "${P#* }"
    unzip -qo "$DL/$b-$FFMPEG_VERSION.zip" -d "$FF"; chmod +x "$FF/$b"; rm -f "$DL/$b-$FFMPEG_VERSION.zip"
    if [ "$OS" = Darwin ]; then xattr -c "$FF/$b" 2>/dev/null || true; fi
    "$FF/$b" -version >/dev/null 2>&1 || fail "$b was downloaded but does not run on this Mac"
  done
  "$FF/ffmpeg" -version | head -1 > "$TOOLS/ffmpeg/VERSION"
fi

# ---- 7 chromium
step browser "Chromium for rendering (Playwright, ~350 MB)"
retry "chromium download" "$VENVPY" -m playwright install chromium || fail "playwright install failed"

# ---- 8 models
step models "AI models: background matte (~14 MB), face detector (~1 MB), speaker labels (~34 MB), whisper turbo (~1.6 GB)"
if [ "$SKIP_MODELS" = 1 ]; then info "skipped (--skip-models)"; else
  RVM="$HOME_DIR/models/rvm/rvm_mobilenetv3_fp32.onnx"
  if [ ! -f "$RVM" ]; then download "$RVM_URL" "$RVM"; else info "RVM already present"; fi
  FACE="$HOME_DIR/models/mediapipe/blaze_face_short_range.tflite"
  if [ ! -f "$FACE" ]; then download "$FACE_URL" "$FACE"; else info "face model already present"; fi
  YUNET="$HOME_DIR/models/yunet/face_detection_yunet_2023mar.onnx"
  if [ -f "$YUNET" ] && [ "$(sha256_of "$YUNET")" != "$YUNET_SHA" ]; then rm -f "$YUNET"; fi
  if [ ! -f "$YUNET" ]; then download "$YUNET_URL" "$YUNET" "$YUNET_SHA"; else info "YuNet face model already present"; fi
  SPK="$HOME_DIR/models/diarize"; mkdir -p "$SPK"
  if [ ! -f "$SPK/pyannote-segmentation-3.0.onnx" ]; then
    download "$SPKSEG_URL" "$DL/spk-seg.tar.bz2" "$SPKSEG_SHA"
    rm -rf "$DL/spk-seg"; mkdir -p "$DL/spk-seg"; tar -xjf "$DL/spk-seg.tar.bz2" -C "$DL/spk-seg" || fail "could not unpack the speaker segmentation model"
    SD="$(dirname "$(find "$DL/spk-seg" -name model.onnx | head -1)")"
    cp "$SD/model.onnx" "$SPK/pyannote-segmentation-3.0.onnx"; cp "$SD/LICENSE" "$SPK/pyannote-segmentation-3.0.LICENSE.txt" 2>/dev/null || true
    rm -rf "$DL/spk-seg" "$DL/spk-seg.tar.bz2"
  else info "speaker segmentation model already present"; fi
  EMB="$SPK/campplus_sv_en_voxceleb_16k.onnx"
  if [ ! -f "$EMB" ]; then download "$SPKEMB_URL" "$EMB" "$SPKEMB_SHA"; else info "speaker embedding model already present"; fi
  info "whisper turbo: downloading (resumes if interrupted; this is the long one)"
  cat > "$DL/prefetch_whisper.py" <<PYEOF
from huggingface_hub import snapshot_download
print(snapshot_download('$WHISPER_REPO', allow_patterns=['config.json','preprocessor_config.json','model.bin','tokenizer.json','vocabulary.*']))
PYEOF
  retry "whisper download" "$VENVPY" "$DL/prefetch_whisper.py" || fail "whisper download failed"
fi

# ---- 9 playbooks
step playbooks "Your playbooks folder (templates only; the reference stays read-only in app/)"
for n in _template _styles; do
  if [ -d "$APP/playbooks/$n" ] && [ ! -d "$HOME_DIR/playbooks/$n" ]; then cp -R "$APP/playbooks/$n" "$HOME_DIR/playbooks/$n"; info "copied $n"; fi
done

# ---- 10 doctor
step doctor "Putting veos on your PATH, then checking everything with veos doctor"
# a stable wrapper in VEOS_HOME/bin (the plugin folder moves with every update); linked into ~/.local/bin or ~/bin when
# one of them is already on PATH (shell profiles are never edited)
mkdir -p "$HOME_DIR/bin"
WRAP_SRC="$(cd "$(dirname "$0")" && pwd)/../bin/veos"; [ -f "$WRAP_SRC" ] || WRAP_SRC="$APP/plugin/bin/veos"
if [ -f "$WRAP_SRC" ]; then
  sed "s|^home=\"\${VEOS_HOME:-\${CLAUDE_PLUGIN_OPTION_VEOS_HOME:-}}\"|home=\"\${VEOS_HOME:-\${CLAUDE_PLUGIN_OPTION_VEOS_HOME:-$HOME_DIR}}\"|" "$WRAP_SRC" > "$HOME_DIR/bin/veos"
  chmod +x "$HOME_DIR/bin/veos"
  LINKED=""
  for d in "$HOME/.local/bin" "$HOME/bin"; do
    case ":$PATH:" in *":$d:"*) if [ -z "$LINKED" ] && [ -d "$d" ]; then ln -sf "$HOME_DIR/bin/veos" "$d/veos" && LINKED="$d"; fi ;; esac
  done
  if [ -n "$LINKED" ]; then info "veos linked into $LINKED"; else info "veos wrapper: $HOME_DIR/bin/veos (add that folder to your PATH to type just 'veos')"; fi
fi
export PATH="$HOME_DIR/bin:$TOOLS/ffmpeg/bin:$PATH"
LIC_EXTRA=""
if [ "$LIC_PENDING" = 1 ]; then
  info "activating your licence (second try)"
  activate_licence
  if [ -n "$LIC_CODE" ]; then
    if [ "$LIC_CODE" = LICENCE_OFFLINE ]; then
      LIC_MSG="Everything is installed, but the licence server couldn't be reached, so the licence isn't activated yet. Check the internet connection, then run /vibe-editing-os:setup licence."
    else
      LIC_MSG="The licence wasn't activated ($LIC_CODE)."
    fi
    info "$LIC_MSG"; log "licence still not activated: $LIC_CODE"
    LIC_EXTRA=",\"licence_pending\":true,\"licence_error\":\"$LIC_CODE\",\"licence_message\":\"$(json_escape "$LIC_MSG")\""
  fi
fi
DOC="$("$VENVPY" -m veos doctor || true)"
READY="$(printf '%s' "$DOC" | "$VENVPY" -c 'import sys,json; print(str(bool(json.load(sys.stdin).get("ready"))).lower())' 2>/dev/null || echo false)"
PROBLEMS="$(printf '%s' "$DOC" | "$VENVPY" -c 'import sys,json; print(json.dumps(json.load(sys.stdin).get("problems",[])))' 2>/dev/null || echo '[]')"
info "doctor ready: $READY"
rm -rf "$DL" "$HOME_DIR/cache"  # uv download cache (~800 MB), not needed after install
printf '{"ok":true,"doctor_ready":%s,"problems":%s,"home":"%s","size_mb":%s,"seconds":%d,"log":"%s"%s}\n' \
  "$READY" "$PROBLEMS" "$(json_escape "$HOME_DIR")" "$(size_of "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")" "$LIC_EXTRA"
