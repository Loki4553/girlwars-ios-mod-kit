@echo off
call "%~dp0tools\setup.bat" || (pause & exit /b 1)
"%~dp0tools\.venv\Scripts\python.exe" "%~dp0tools\kit_convert.py"
pause
