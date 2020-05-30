@echo off
title Windows Distribution Script

if not [%3]==[] (
echo Too many arguments...
goto:eof
) 

if not "%1"=="-v" (
echo Must use -v flag...
goto:eof
)

set dir=SSHshare-v%2-x64-Win10
echo Preparing %dir%...
mkdir %dir%
copy SSHshare.exe %dir% 
copy webview.dll %dir%
copy WebView2Loader.dll %dir%
zip -r %dir%.zip %dir%
copy %dir%.zip Z:\SSHshare\
echo All Done!



