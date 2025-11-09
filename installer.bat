@echo off
setlocal EnableDelayedExpansion

color 6
echo [LOG] Installing requirements.txt
pip install -r requirements.txt

echo [LOG] Requirements Installed!

echo
echo
echo If the script fails...
echo Rerun installer.bat with admin privileges

PAUSE
cls

