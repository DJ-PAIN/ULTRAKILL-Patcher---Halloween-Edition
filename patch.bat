@echo off
:: Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Change to the directory where the batch file is located
cd /d "%~dp0"

:: Run the Python script
pip install colorama
pip install psutil
cls
python patch.py
pause
