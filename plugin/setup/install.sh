#!/usr/bin/env bash
# Vibe Editing OS - one-time installer (macOS arm64 first, Linux best-effort). No sudo, nothing outside VEOS_HOME.
# Idempotent + resumable. Re-run any time; --update refreshes the app.
#
#   --home DIR         VEOS_HOME (default ~/Library/Application Support/VibeEditingOS)
#   --app-source DIR   copy the app from a local checkout instead of git/zip (testing).  env VEOS_APP_SOURCE
#   --repo URL         GitHub repo (https://github.com/namansoniai/vibe-editing-os).        env VEOS_REPO
#   --ref NAME         branch/tag (default main).                                        env VEOS_REF
#   --update           pull a new app version and reinstall the engine if it changed
#   --skip-models      skip the ~1.7 GB model downloads
# Output: one progress line per step, final line JSON {"ok":true|false,...}. Log: VEOS_HOME/install.log
set -u

UV_VERSION="0.12.23"
RVM_URL="https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx"
FACE_URL="https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite"
WHISPER_REPO="mobiuslabsgmbh/faster-whisper-large-v3-turbo"
TOTAL=10

OS="$(uname -s)"; ARCH="$(uname -m)"
# a shell running under Rosetta reports x86_64 on Apple Silicon; we still want the native arm64 tools
if [ "$OS" = Darwin ] && [ "$ARCH" = x86_64 ] && [ "$(sysctl -n hw.optional.arm64 2>/dev/null || echo 0)" = 1 ]; then ARCH=arm64; fi
# DRY_RUN=1 [DRY_PLATFORM=Darwin-arm64]: print + HEAD-check every URL for that platform, install nothing
DRY_RUN="${DRY_RUN:-0}"
if [ -n "${DRY_PLATFORM:-}" ]; then OS="${DRY_PLATFORM%%-*}"; ARCH="${DRY_PLATFORM#*-}"; fi
DEFAULT_REPO="https://github.com/namansoniai/vibe-editing-os-dist"
case "$OS" in
  Darwin) DEFAULT_HOME="$HOME/Library/Application Support/VibeEditingOS" ;;
  *) DEFAULT_HOME="${XDG_DATA_HOME:-$HOME/.local/share}/VibeEditingOS" ;;
esac
HOME_DIR="${VEOS_HOME:-$DEFAULT_HOME}"
APP_SOURCE="${VEOS_APP_SOURCE:-}"
REPO="${VEOS_REPO:-$DEFAULT_REPO}"
REF="${VEOS_REF:-main}"
UPDATE=0; SKIP_MODELS=0
while [ $# -gt 0 ]; do
  case "$1" in
    --home) HOME_DIR="$2"; shift 2 ;;
    --app-source) APP_SOURCE="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --ref) REF="$2"; shift 2 ;;
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
    app) echo "Check your internet connection. For a private repo make sure git is installed and signed in to GitHub, then re-run." ;;
    uv|python|ffmpeg|browser|models) echo "Check your internet connection and re-run; the installer resumes where it stopped." ;;
    doctor) echo "Run veos doctor and follow the hint on the failing check." ;;
    *) echo "Re-run the installer. If it persists, send the last lines of install.log." ;;
  esac
}
fail() {
  local msg="$1"
  log "FAILED at $STEP: $msg"; echo "FAILED at step '$STEP': $msg"
  printf '{"ok":false,"step":"%s","error":"%s","hint":"%s","home":"%s","seconds":%d,"log":"%s"}\n' \
    "$STEP" "$(json_escape "$msg")" "$(json_escape "$(hint_for "$STEP")")" "$(json_escape "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")"
  exit 1
}
trap 'fail "unexpected error (line $LINENO)"' ERR
set -e

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
download() { # download <url> <out> [sha256]
  local url="$1" out="$2" sha="${3:-}" i got
  mkdir -p "$(dirname "$out")"
  for i in 1 2 3; do
    rm -f "$out"
    if curl -fL --retry 2 -sS -o "$out" "$url"; then
      if [ -n "$sha" ]; then
        got="$(sha256_of "$out")"
        if [ "$got" != "$sha" ]; then log "sha mismatch $got"; [ "$i" -lt 3 ] && continue; fail "sha256 mismatch for $(basename "$out"): expected $sha got $got"; fi
      fi
      info "downloaded $(basename "$out") ($(( $(wc -c < "$out") / 1048576 )) MB)"
      return 0
    fi
    [ "$i" -lt 3 ] && { info "network hiccup, retrying ($i/3)..."; sleep $((3*i)); }
  done
  fail "download failed after 3 tries: $url"
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
ffmpeg_target() {
  case "$OS-$ARCH" in
    Darwin-arm64) echo "macos/arm64" ;;
    Darwin-x86_64) echo "macos/amd64" ;;
    Linux-x86_64) echo "linux/amd64" ;;
    Linux-aarch64) echo "linux/arm64" ;;
    *) return 1 ;;
  esac
}
UV_BASE="https://github.com/astral-sh/uv/releases/download/$UV_VERSION"
# the "redirect/latest" URL redirects to the versioned file; resolve it so the .sha256 sits next to the real file
ffmpeg_url() {
  local r="https://ffmpeg.martin-riedl.de/redirect/latest/$(ffmpeg_target)/release/$1.zip" f
  f="$(curl -sS -m 30 -L -r 0-0 -o /dev/null -w '%{url_effective}' "$r" 2>/dev/null || true)"
  case "$f" in https://*.zip) echo "$f" ;; *) echo "$r" ;; esac
}

if [ "$DRY_RUN" = 1 ]; then
  bad=0
  check() { code="$(curl -sS -m 30 -L -r 0-0 -o /dev/null -w '%{http_code}' "$1" 2>/dev/null || echo 000)"; echo "$code $1"; case "$code" in 200|206) ;; *) bad=1 ;; esac; }
  echo "DRY RUN for $OS-$ARCH (nothing is installed)"
  UVT="$(uv_target)" || { echo "unsupported platform"; exit 1; }
  check "$UV_BASE/uv-$UVT.tar.gz"; check "$UV_BASE/uv-$UVT.tar.gz.sha256"
  for b in ffmpeg ffprobe; do check "$(ffmpeg_url $b)"; check "$(ffmpeg_url $b).sha256"; done
  check "$RVM_URL"; check "$FACE_URL"
  check "https://huggingface.co/$WHISPER_REPO/resolve/main/config.json"
  if command -v git >/dev/null 2>&1; then
    if GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code "$REPO.git" HEAD >/dev/null 2>&1; then echo "ok git access to $REPO"; else echo "NOTE: git cannot read $REPO yet (private repo: sign in once with gh auth login)"; fi
  fi
  echo "would run: uv python install 3.12; uv venv; uv export --frozen | uv pip sync; uv pip install -e app/engine; python -m playwright install chromium; veos doctor"
  exit $bad
fi

# process-scoped environment only
export VEOS_HOME="$HOME_DIR"
export UV_PYTHON_INSTALL_DIR="$HOME_DIR/python"
export UV_CACHE_DIR="$HOME_DIR/cache/uv"
export UV_PYTHON_PREFERENCE=only-managed
export UV_LINK_MODE=copy
export UV_NO_PROGRESS=1
export PLAYWRIGHT_BROWSERS_PATH="$HOME_DIR/browsers"
export HF_HOME="$HOME_DIR/models/hf"
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
export PYTHONIOENCODING=utf-8 PYTHONUTF8=1
export GIT_TERMINAL_PROMPT=0

# ---- 1 home
step home "Preparing $HOME_DIR"
mkdir -p "$HOME_DIR"/{tools,browsers,models/rvm,models/mediapipe,models/hf,playbooks,scratch,cache}

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
else
  if [ -z "$REPO" ]; then
    PJ="$(cd "$(dirname "$0")" && pwd)/../.claude-plugin/plugin.json"
    [ -f "$PJ" ] && REPO="$(sed -n 's/.*"repository"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$PJ" | head -1)"
  fi
  case "$REPO" in "") fail "repository not configured: set VEOS_REPO=https://github.com/<owner>/vibe-editing-os (or --app-source DIR)" ;; esac
  case "$REPO" in http*) ;; *) REPO="https://github.com/$REPO" ;; esac
  REPO="${REPO%/}"; REPO="${REPO%.git}"
  DONE=0
  SLUG="${REPO#https://github.com/}"
  # 1) plain HTTPS zip first: works for the public distribution repo with no git, no developer tools, no sign-in
  fetch_zip() {
    download "https://codeload.github.com/$SLUG/zip/refs/heads/$REF" "$DL/app.zip" || return 1
    rm -rf "$DL/app-x"; mkdir -p "$DL/app-x"; unzip -q "$DL/app.zip" -d "$DL/app-x" || return 1
    TOP="$(ls -d "$DL"/app-x/*/ | head -1)"
    rm -rf "$APP"; mkdir -p "$APP"
    for d in $APPDIRS; do [ -d "$TOP$d" ] && cp -R "$TOP$d" "$APP/$d"; done
    rm -rf "$DL/app.zip" "$DL/app-x"
  }
  info "downloading the app ($SLUG, $REF)"
  if fetch_zip; then DONE=1; fi
  # 2) git fallback (private repos). On macOS only if developer tools exist, so we never trigger the install pop-up
  git_ok=0
  if command -v git >/dev/null 2>&1; then
    if [ "$OS" = Darwin ]; then xcode-select -p >/dev/null 2>&1 && git_ok=1; else git_ok=1; fi
  fi
  if [ "$DONE" = 0 ] && [ "$git_ok" = 1 ]; then
    info "zip download failed; trying git with your saved git credentials"
    clone() { rm -rf "$APP"; git clone --depth 1 --branch "$REF" --filter=blob:none --sparse "$REPO" "$APP"                 && git -C "$APP" sparse-checkout set $APPDIRS; }
    if retry "git clone" clone; then DONE=1; fi
  fi
  [ "$DONE" = 1 ] || fail "could not download the app from $REPO (check the internet connection; for a private repo, sign in to GitHub first)"
fi
for d in $APPDIRS; do [ -d "$APP/$d" ] || fail "app is incomplete: $d missing"; done
AFTER="$(hash_of)"
info "app ready at $APP"

# ---- 3 uv
step uv "uv $UV_VERSION (Python manager)"
if [ -x "$UV" ] && "$UV" --version 2>/dev/null | grep -q "$UV_VERSION"; then info "already installed"; else
  UVT="$(uv_target)" || fail "unsupported platform $OS-$ARCH"
  ASSET="uv-$UVT.tar.gz"; BASE="$UV_BASE/$ASSET"
  SHA="$(curl -fsSL "$BASE.sha256" | awk '{print $1}')"
  download "$BASE" "$DL/$ASSET" "$SHA"
  rm -rf "$DL/uv-x"; mkdir -p "$DL/uv-x" "$TOOLS/uv"; tar -xzf "$DL/$ASSET" -C "$DL/uv-x"
  cp "$(dirname "$(find "$DL/uv-x" -name uv -type f | head -1)")"/uv* "$TOOLS/uv/"; chmod +x "$TOOLS/uv/"*
  rm -rf "$DL/$ASSET" "$DL/uv-x"
fi
[ -x "$UV" ] || fail "uv missing after install"

# ---- 4 python + venv
step python "Python 3.12 + virtual environment (~70 MB)"
retry "python download" "$UV" python install 3.12 || fail "uv python install failed"
[ -x "$VENVPY" ] || "$UV" venv "$VENV" --python 3.12

# ---- 5 engine
step engine "Installing the veos engine and its packages (~700 MB)"
HAVE=""; [ -f "$STATE/engine.sha" ] && HAVE="$(cat "$STATE/engine.sha")"
IMPORT_OK=0
if [ "$HAVE" = "$AFTER" ] && "$VENVPY" -c "import veos, faster_whisper, onnxruntime, playwright, cv2, mediapipe" >/dev/null 2>&1; then IMPORT_OK=1; fi
if [ "$IMPORT_OK" = 1 ]; then info "engine packages already match the app version"; else
  "$UV" export --project "$APP/engine" --frozen --no-dev --no-emit-project --no-hashes -o "$DL/requirements.txt" -q
  retry "package download" "$UV" pip sync --python "$VENVPY" "$DL/requirements.txt" || fail "uv pip sync failed"
  # editable: the engine finds renderer/, assets/, playbooks/ relative to app/engine/src
  retry "engine install" "$UV" pip install --python "$VENVPY" --no-deps -e "$APP/engine" || fail "engine install failed"
  rm -f "$DL/requirements.txt"; echo "$AFTER" > "$STATE/engine.sha"
fi

# ---- 6 ffmpeg
step ffmpeg "ffmpeg + ffprobe (static build, checksum-verified)"
FF="$TOOLS/ffmpeg/bin"
if [ -x "$FF/ffmpeg" ] && [ -x "$FF/ffprobe" ]; then info "already installed"; else
  mkdir -p "$FF"
  ffmpeg_target >/dev/null || fail "unsupported platform $OS-$ARCH"
  for b in ffmpeg ffprobe; do
    U="$(ffmpeg_url $b)"
    SHA="$(curl -fsSL "$U.sha256" 2>/dev/null | awk '{print $1}' || true)"
    download "$U" "$DL/$b.zip" "$SHA"
    unzip -qo "$DL/$b.zip" -d "$FF"; chmod +x "$FF/$b"; rm -f "$DL/$b.zip"
    if [ "$OS" = Darwin ]; then xattr -c "$FF/$b" 2>/dev/null || true; fi
    "$FF/$b" -version >/dev/null 2>&1 || fail "$b was downloaded but does not run on this Mac"
  done
  "$FF/ffmpeg" -version | head -1 > "$TOOLS/ffmpeg/VERSION"
fi

# ---- 7 chromium
step browser "Chromium for rendering (Playwright, ~350 MB)"
retry "chromium download" "$VENVPY" -m playwright install chromium || fail "playwright install failed"

# ---- 8 models
step models "AI models: background matte (~14 MB), face detector (~1 MB), whisper turbo (~1.6 GB)"
if [ "$SKIP_MODELS" = 1 ]; then info "skipped (--skip-models)"; else
  RVM="$HOME_DIR/models/rvm/rvm_mobilenetv3_fp32.onnx"
  if [ ! -f "$RVM" ]; then download "$RVM_URL" "$RVM.part"; mv "$RVM.part" "$RVM"; else info "RVM already present"; fi
  FACE="$HOME_DIR/models/mediapipe/blaze_face_short_range.tflite"
  if [ ! -f "$FACE" ]; then download "$FACE_URL" "$FACE.part"; mv "$FACE.part" "$FACE"; else info "face model already present"; fi
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
step doctor "Checking everything with veos doctor"
export PATH="$TOOLS/ffmpeg/bin:$PATH"
DOC="$("$VENVPY" -m veos doctor || true)"
READY="$(printf '%s' "$DOC" | "$VENVPY" -c 'import sys,json; print(str(bool(json.load(sys.stdin).get("ready"))).lower())' 2>/dev/null || echo false)"
PROBLEMS="$(printf '%s' "$DOC" | "$VENVPY" -c 'import sys,json; print(json.dumps(json.load(sys.stdin).get("problems",[])))' 2>/dev/null || echo '[]')"
info "doctor ready: $READY"
rm -rf "$DL" "$HOME_DIR/cache"  # uv download cache (~800 MB), not needed after install
printf '{"ok":true,"doctor_ready":%s,"problems":%s,"home":"%s","size_mb":%s,"seconds":%d,"log":"%s"}\n' \
  "$READY" "$PROBLEMS" "$(json_escape "$HOME_DIR")" "$(size_of "$HOME_DIR")" $(( $(date +%s) - T0 )) "$(json_escape "$LOG")"
