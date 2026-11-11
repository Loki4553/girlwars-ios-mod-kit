@echo off
set "PY=%~dp0.venv\Scripts\python.exe"
rem Ready already? (checks the library really works, not just that Python is there)
if exist "%PY%" "%PY%" -c "import UnityPy" 2>nul && exit /b 0

if not exist "%PY%" (
  echo First run: setting up, about 1 minute, needs internet. Don't close this window...
  py -3 -m venv "%~dp0.venv" 2>nul || python -m venv "%~dp0.venv" 2>nul
) else (
  echo Finishing an unfinished setup, needs internet. Don't close this window...
)
if not exist "%PY%" (
  echo.
  echo Python is not installed. Install it from https://www.python.org/downloads/
  echo and tick "Add python.exe to PATH" during install. Then run this again.
  exit /b 1
)
"%PY%" -m pip install --disable-pip-version-check --progress-bar off UnityPy==1.25.4
"%PY%" -c "import UnityPy" 2>nul && (echo Setup done. & echo. & exit /b 0)
echo.
echo Setup failed. Check your internet connection and run this again.
exit /b 1
