@echo off
if "%~1"=="" (
  echo Drag a DECRYPTED Girl Wars .ipa file onto this .bat file.
  pause
  exit /b 1
)
call "%~dp0tools\setup.bat" || (pause & exit /b 1)
"%~dp0tools\.venv\Scripts\python.exe" "%~dp0tools\kit_ipa.py" "%~1"
pause
