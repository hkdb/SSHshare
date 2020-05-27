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

if [ ! -d ~/.local/bin ]; then
    echo "~/.local/bin doesn't exist... Creating..."
    mkdir -p ~/.local/bin
fi

if [ ! -d ~/.local/share/applications ]; then
    echo "~/.local/share/applications doesn't exist... Creating..."
    mkdir -p ~/.local/share/applications   
fi

if [ ! -d ~/.local/share/icons/hicolor/256x256 ]; then
    echo "~/.local/share/icons/hicolor/256x256 doesn't exist... Creating..."
    mkdir -p ~/.local/share/icons/hicolor/256x256
fi

echo "Installing icon..."
cp SSHshare-icon.png ~/.local/share/icons/hicolor/256x256/

echo "Installing .desktop..."
# Generate .desktop
cat > ~/.local/share/applications/SSHshare.desktop <<EOF
[Desktop Entry]
Version=0.2.0
Name=SSHshare
Comment=GUI Encrypt/Decrypt w/ ssh-vault
GenericName=SSHshare
Exec=$HOME/.local/bin/SSHshare
Path=$HOME/.local/bin/
Terminal=false
Type=Application
Icon=$HOME/.local/share/icons/hicolor/256x256/SSHshare-icon.png
StartupNotify=true
Categories=Utility;
EOF

echo "Installing binary..."
cp SSHshare ~/.local/bin/
chmod +x ~/.local/bin/SSHshare

echo ""

echo "Entering ~/local/bin..."
cd ~/.local/bin/

if [ -f "~/.local/bin/ssh-vault" ];
then
    echo "SSH-Vault doesn't exist... Installing..."
    wget https://bintray.com/nbari/ssh-vault/download_file?file_path=ssh-vault_0.12.6_linux_amd64.tar.gz
    tar -xzvf ssh-vault_0.12.6_linux_amd64.tar.gz
    mv ssh-vault_0.12.6_linux_amd64/ssh-vault .
    chmod +x ssh-vault
    rm -rf ssh-vault_0.12.6_linux_amd64
    rm ssh-vault_0.12.6_linux_amd64.tar.gz
else
    echo "SSH-Vault is already installed... Skipping..."
fi

echo ""

echo "Installation Complete. If you don't see any errors above, you are good to go! :)"
