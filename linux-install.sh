#!/bin/bash

#################################################################
### PROJECT:
### SSHshare
### VERSION:
### v0.1.0
### SCRIPT:
### install.sh
### DESCRIPTION:
### Install Script for SSHshare
### MAINTAINED BY:
### hkdb <hkdb@3df.io>
### Disclaimer:
### This application is maintained by volunteers and in no way
### do the maintainers make any guarantees. Use at your own risk.
### ##############################################################

wget https://bintray.com/nbari/ssh-vault/download_file?file_path=ssh-vault_0.12.4_linux_amd64.tar.gz
mv 'download_file?file_path=ssh-vault_0.12.4_linux_amd64.tar.gz' ssh-vault_0.12.4_linux_amd64.tar.gz 
tar -xzvf ssh-vault_0.12.4_linux_amd64.tar.gz
cp ./ssh-vault_0.12.4_linux_amd64/ssh-vault ~/.local/bin/
chmod u+x ~/.local/bin/ssh-vault
chmod a+x SSHshare.py
chmod a+x SSHshare.desktop
cp SSHshare.desktop /usr/share/applications/
echo "Installation Complete. If you don't see any errors above, you are good to go! :)"
