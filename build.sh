#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    go build -o linux/SSHshare
elif [[ "$OSTYPE" == "darwin19" ]]; then
    go build -o macos/SSHshare
elif [[ "$OSTYPE" == "darwin17" ]]; then
    go build -o macos/SSHshare
else
    echo "$OSTYPE is not a supported platform"
fi