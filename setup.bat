@echo off
rem ---- one-time setup: makes .venv and installs pygame-ce ----
setlocal
pushd "%~dp0"

echo Making a private Python for this project...
python -m venv .venv
if errorlevel 1 goto :nopython

echo Installing pygame-ce...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt

echo.
echo Done. Try:   .\run.bat 1
popd
pause
exit /b 0

:nopython
echo.
echo Could not find Python. Install it from python.org first,
echo and tick "Add python.exe to PATH" during the install.
popd
pause
exit /b 1
