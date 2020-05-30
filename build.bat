@echo off
title Windows Build Script

go generate
go build -ldflags="-H windowsgui -linkmode internal" -o win/SSHshare.exe