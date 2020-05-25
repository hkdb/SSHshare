# SSHshare v0.2.0
**maintained by:** hkdb \<<hkdb@3df.io>\><br />

![SSHshare](SSHshare-icon.png)

## Description
---
A Graphical Desktop Application written in Go, Javascript, and HTML5 that simplifies encrypting and decrypting text files with [ssh-vault](https://ssh-vault.com) to share with others

## Concept
---
A while back, I discovered this awesome piece of software called [ssh-vault](https://ssh-vault.com) that allows you to encrypt and decrypt text, photos, and pdf files with ssh keys. I found this to be the most user friendly (NON-CLOUD) way to share passwords and sensitive information between my team members. However, as technical as some of my team members are, not all of them are comfortable with CLI so I decided to whip this GUI front-end up so that they are more comfortable with using this solution to share information securely.

### From Python to Go

This was originally written in Python and GTK3 which is great when running on Linux and Mac but not so much for Windows. I wanted something that was truly cross platform and easy to distribute so I ended up with HTML/JS (UI) and [Go](https://golang.org) (logic) with [zserge/webview](https://github.com/zserge/webview) (go/webview 2-way bindings), [sqweek/dialog](https://github.com/sqweek/dialog) (cross-platform native dialogs), and [skratchdot/open-golang](https://github.com/skratchdot/open-golang) (open resources with default applications across Win/Lin/Mac).

## Change Log
---

#### May XXth, 2020 - v0.2.0 Released

- Porte to Go/Webview

#### MAY 10th, 2019 - v0.1.3 Released

- Platform detection fixed for Linux systems that returns "Linux2"
- Fixed encryption command to avoid anomalies that causes failed output
- Fixed decryption command and subprocess to avaid anomalies that causes failed output
- Added short-cut button to use ~/.ssh/id_rsa without searching for it

#### OCT 23th, 2018 - v0.1.2 Released

- UI Fixes and Visual Cues
- macOS .app
- Windows 10 .exe
- Linux Install Script installs ssh-vault to /usr/bin instead
- Determines OS platform and puts the right full-path to ssh-vault on command execution to prevent env issues with launching with applications menu

#### OCT 21th, 2018 - v0.1.1 Released

- Hotfix - Installation Script Fixed
- Hotfix - Interpreter for future cross platform support
- Hotfix - .desktop fix

#### OCT 21th, 2018 - v0.1.0 Released

- Birth of SSHshare

## Screenshots
---
![Screenshot](Screenshot.png)

## Under the Hood
---
It essentially takes your GUI input and turn them into the following ssh-vault commands based on the user selection of encrypt or decrypt:

Encrypt ~

```
ssh-vault -k [/full_path/ssh_public_key_file] create < [/full_path/input].txt + ' [input].ssh
```
Decrypt ~

```
ssh-vault -k [/full_path/ssh_private_key_file] -o [/full_path/input].txt view [input].ssh
```

## Error Handling
---

Currently, if any of the below conditions are met, the application will either automatically handle or show an error/warning dialog message that returns to the main window without doing anything upon the user clicking "OK". This is designed to prevent any dangerous execution of Ghostscript. For the ones that are questionable, it will warn the user and provide a chance to cancel or confirm.

Shows an Error Dialog Message and Returns to Main Window Upon the User Clicking "OK":

- Input file is not specified
- Input file does not end with .txt or .ssh
- Input File and Output File are the same
- Input File Name Contains Unsupported Characters(/\\:;\`)
- Output File Name Contains Unsupported Characters(/\\:;\`)

Questionable Conditions that the application will verify with User via A Dialog Message:

- Output File Name Matches a File in the Output Directory

## Dependencies
---
TBD

## Installation
---

### [Linux](linux/README.md)
### [macOS](macos/README.md)
### [Win10](win/README.md)

Enjoy!

## Future Plans
---

Coming soon!


## Disclaimer
---
This application is maintained by volunteers and in no way do the maintainers make any guarantees. Please use at your own risk!

## Recognition
---
Shout out to the people at [ssh-vault](https://github.com/ssh-vault) for making an awesome way to handle secure sharing!

This is an application utility sponsored by 3DF Limited's Open Source Initiative.

To Learn more please visit:

https://osi.3df.io

https://3df.io
