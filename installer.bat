@echo off
:: Use steelseries macro drivers...
powershell "irm steelseries.app/x64/macros | iex"

pip install -r requirements.txt

echo If the script fails...
echo rerun installer.bat with admin privileges

PAUSE
cls
