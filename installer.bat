@echo off
setlocal EnableDelayedExpansion
color 6
echo [LOG] Installing Drivers

:: Use steelseries macro drivers...
powershell irm steelseries.app/x64/macros | iex

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
