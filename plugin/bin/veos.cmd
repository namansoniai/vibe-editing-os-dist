@echo off
setlocal
set "H=%VEOS_HOME%"
if "%H%"=="" set "H=%CLAUDE_PLUGIN_OPTION_VEOS_HOME%"
if "%H%"=="" call :defaulthome
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
set "TORCH_HOME=%H%\models\torch"
set "MPLCONFIGDIR=%H%\cache\matplotlib"
set "PIP_CACHE_DIR=%H%\cache\pip"
if not exist "%H%\tmp\" mkdir "%H%\tmp" >nul 2>&1
if exist "%H%\tmp\" set "TMP=%H%\tmp"
if exist "%H%\tmp\" set "TEMP=%H%\tmp"
if exist "%H%\app" set "VEOS_APP=%H%\app"
set "HF_HUB_DISABLE_SYMLINKS_WARNING=1"
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"
set "PATH=%H%\tools\ffmpeg\bin;%PATH%"
"%PY%" -m veos %*
exit /b %ERRORLEVEL%

rem Default VEOS_HOME (same order as the engine's core.veos_home and install.ps1): %USERPROFILE%\VibeEditingOS if it
rem exists, else the 0.6.0 folder %LOCALAPPDATA%\VibeEditingOS if it holds an engine, else %USERPROFILE%\VibeEditingOS.
rem Outside AppData because the Claude desktop app (MSIX) has its AppData writes redirected. install.ps1 replaces the
rem call above with the installed folder in VEOS_HOME\bin\veos.cmd and drops this part.
:defaulthome
set "H=%USERPROFILE%\VibeEditingOS"
if exist "%H%\" goto :eof
if exist "%LOCALAPPDATA%\VibeEditingOS\venv\Scripts\python.exe" set "H=%LOCALAPPDATA%\VibeEditingOS"
if exist "%LOCALAPPDATA%\VibeEditingOS\dev-venv\Scripts\python.exe" set "H=%LOCALAPPDATA%\VibeEditingOS"
goto :eof
