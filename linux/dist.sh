#!/bin/bash

POSITIONAL=()

if [ "$#" != 2 ] && [ "$1" != "-h" ]; then
    echo -e '\nSomething is missing... Type "./setup -h" without the quotes to find out more...\n'
    exit 0
fi

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -v|--version)
    VERSION="$2"
    shift # past argument
    shift # past value
    ;;
    -h|--help)
    echo -e "\nVBoxMacSetup $VERSION\n\nOPTIONS:\n\n-v, --vm: Virtual Machine Name\n-r, --resolution: VM Resolution\n-h, --help: Help\n\nEXAMPLE:\n\n./setup.sh -v MacOS -r 1920x1080\n"
    exit 0
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

DIR="SSHshare-v$VERSION-x64-Linux"
mkdir $DIR
cp SSHshare $DIR/ 
cp ../SSHshare-icon.png $DIR
cp install.sh $DIR/
tar -cjvf SSHshare-v$VERSION-x64-Linux.tar.bz2 $DIR 