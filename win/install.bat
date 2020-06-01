@echo off
title Windows Installation Script

echo Setting policy to allow localhost web server...
powershell -command "start-process -verb runAs 'CheckNetIsolation.exe' -argumentlist 'LoopbackExempt -a -n=\"Microsoft.Win32WebViewHost_cw5n1h2txyewy\"'

rem SSHshare
xcopy /y /s /i "SSHshare" "C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare"

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "C:\Users\%USERNAME%\Desktop\SSHshare.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare\SSHshare.exe" >> %SCRIPT%
echo oLink.WorkingDirectory ="C:\Users\%USERNAME%\AppData\Local\Programs\SSHshare" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%

del %SCRIPT%