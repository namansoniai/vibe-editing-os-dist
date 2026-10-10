@echo off
setlocal
set "H=%VEOS_HOME%"
if "%H%"=="" set "H=%CLAUDE_PLUGIN_OPTION_VEOS_HOME%"
if "%H%"=="" set "H=%LOCALAPPDATA%\VibeEditingOS"
set "PY="
if exist "%H%\venv\Scripts\python.exe" set "PY=%H%\venv\Scripts\python.exe"
if "%PY%"=="" if exist "%H%\dev-venv\Scripts\python.exe" set "PY=%H%\dev-venv\Scripts\python.exe"
if "%PY%"=="" (
  echo {"ok":false,"error":{"code":"ENGINE_MISSING","hint":"run /vibe-editing-os:setup"}}
  exit /b 1
)
set "VEOS_HOME=%H%"
set "PLAYWRIGHT_BROWSERS_PATH=%H%\browsers"
set "HF_HOME=%H%\models\hf"
if exist "%H%\app" set "VEOS_APP=%H%\app"
set "HF_HUB_DISABLE_SYMLINKS_WARNING=1"
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"
set "PATH=%H%\tools\ffmpeg\bin;%PATH%"
"%PY%" -m veos %*
exit /b %ERRORLEVEL%
