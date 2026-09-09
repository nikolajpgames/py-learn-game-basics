@echo off
rem ---- run.bat 6   ->  runs session 6 ----
setlocal
pushd "%~dp0"

if "%~1"=="" (
  echo Usage:  .\run.bat 6
  popd & exit /b 1
)

set "TARGET="
for /d %%D in ("sessions\s%~1_*" "sessions\s0%~1_*") do set "TARGET=%%D"

if not defined TARGET (
  echo There is no session %~1 yet.
  popd & exit /b 1
)

set "PY=%CD%\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

rem run from inside the session's own folder, so it can find its own files
pushd "%TARGET%"
"%PY%" main.py
popd
popd
