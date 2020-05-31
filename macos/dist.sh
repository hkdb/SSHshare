#!/bin/bash

VERSION="v0.1"

POSITIONAL=()

if [ "$#" != 2 ] && [ "$1" != "-h" ]; then
    echo -e '\nSomething is missing... Type "./dist.sh -h" without the quotes to find out more...\n'
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
    echo -e "\ninstall.sh $VERSION\n\nOPTIONS:\n\n-v: Version Number\n-h, --help: Help\n\nEXAMPLE:\n\n./setup.sh -v MacOS -r 1920x1080\n"
    exit 0
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

DIR="SSHshare-v$VERSION-x64-MacOS"

cp ./SSHshare ./SSHshare.app/Contents/MacOS/
./make_dmg \
    -image dmgback.png \
    -file 144,144 SSHshare.app \
    -symlink 416,144 /Applications \
    -convert UDBZ \
    $DIR.dmg


