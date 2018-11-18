# SSHshare v0.1.2
**maintained by:** hkdb \<<hkdb@3df.io>\><br />

## Description
---
A GTK+ GUI Application written in Python that simplifies encrypting and decrypting text files with [ssh-vault](https://ssh-vault.com) to share with others

## Concept
---
A while back, I discovered this awesome piece of software called [ssh-vault](https://ssh-vault.com) that allows you to encrypt and decrypt text, photos, and pdf files with ssh keys. I found this to be the most user friendly way to share passwords and sensitive information between my team members. However, as technical as some of my team members are, not all of them are comfortable with CLI so I decided to whip this GUI front-end up so that they are more comfortable with using this solution to share information securely. 

## Change Log
---
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
![Screenshot](https://osi.3df.io/wp-content/uploads/2018/10/SSHshare-ScreenShot.png)

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

- Python 3
- GTK+ 3
- pygobject
- gi

## Installation
---

### [Linux](##Installation)

1. Verify that there's a ~/.local/bin and if not, make the directory and make sure it's configured properly in your environment.
2. Move SSHshare directory to /opt/
3. Change into /opt/SSHshare/
4. Run Install Script:

```
sudo chmod u+x linux-install.sh
sudo ./linux-install.sh
```
### [macOS](Mac.md)
### [Win10](Win.md)

Enjoy!

## Future Plans
---
- Mac and Windows Support
- More User Friendly Features

## Disclaimer
---
This application is maintained by volunteers and in no way do the maintainers make any guarantees. Please use at your own risk!

## Recognition
---
Shout out to the people at [ssh-vault](https://github.com/ssh-vault) for making an awesome way to handle secure sharing!

This is an application utility sponsored by 3DF Limited's Open Source Initiative.

To Learn more please visit:

https://osi.3df.io

https://www.3df.com.hk
