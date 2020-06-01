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
mkdir %dir%\SSHshare
wget -O ssh-vault_0.12.6_windows_amd64.zip https://bintray.com/nbari/ssh-vault/download_file?file_path=ssh-vault_0.12.6_windows_amd64.zip
unzip -n ssh-vault_0.12.6_windows_amd64.zip
move ssh-vault.exe %dir%\SSHshare
del LICENSE
del ssh-vault_0.12.6_windows_amd64.zip
copy SSHshare.exe %dir%\SSHshare 
copy webview.dll %dir%\SSHshare
copy WebView2Loader.dll %dir%\SSHshare
copy install.bat %dir%
zip -r %dir%.zip %dir%
echo All Done!



