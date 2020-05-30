@echo off
title Windows Installation Script

rem ssh-vault
if not exist C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps (
    echo Installing ssh-vault...
    copy ssh-vault C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps\
) else (
    echo ssh-vault exists... skipping...
)

rem SSHshare
xcopy /s /i "SSHshare" "C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare"

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "C:\Users\%USERNAME%\Desktop\SSHshare.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare\SSHshare.exe" >> %SCRIPT%
echo oLink.WorkingDirectory ="C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%

del %SCRIPT%