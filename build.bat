@echo off
title Windows Build Script

go build -ldflags="-H windowsgui" -o win/SSHshare.exe