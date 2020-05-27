#!/bin/bash

#################################################################
### PROJECT:
### SSHshare
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

echo "Beginning Installation."

echo ""

echo "Installing binary..."
sudo cp -R SSHshare.app /Applications/

echo ""

if [ ! -d "/usr/local/Cellar" ];
then
    echo "SSH-Vault doesn't exist... Installing..."
    brew install ssh-vault
else
    echo "SSH-Vault is already installed... Skipping..."
fi

echo ""

echo "Installation Complete. If you don't see any errors above, you are good to go! :)"
