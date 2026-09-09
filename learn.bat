@echo off
rem ---- learn.bat 6   ->  opens the lesson page for session 6 ----
setlocal
pushd "%~dp0"

if "%~1"=="" (
  echo Usage:  .\learn.bat 6
  popd & exit /b 1
)

set "TARGET="
for /d %%D in ("sessions\s%~1_*" "sessions\s0%~1_*") do set "TARGET=%%D"

if not defined TARGET (
  echo There is no session %~1 yet.
  popd & exit /b 1
)

start "" "%TARGET%\lesson.html"
popd
