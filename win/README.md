# Windows 10 64-bit

maintained by: hkdb `<hkdb@3df.io>`

### Dependancies:

- OpenSSH
- ssh-vault
- [Scoop](https://scoop.sh)
    - wget
    - gcc (Development Only)
    - Go (Development Only)

### Delta:

ssh-vault will be installed at C:\Users\<username>\AppData\Local\Microsoft\WindowsApps

The two DLL files must be in the same directory as the compiled exe for it to run properly.

### Compiling:

Execute the following if you are compiling for the first time:

Open Powershell as Administrator:
```
PS C:\WINDOWS\system32> CheckNetIsolation.exe LoopbackExempt -a -n="Microsoft.Win32WebViewHost_cw5n1h2txyewy"
```
Note: This is to allow hosting a webserver on localhost which is the backend of the application

From the cloned repo:

```
go get
```

If it doesn't work, you may need to do the following:
```
go get -u github.com/zserge/webview
```
Execute the following scripts starting at the top level of the repo:

```
./build.bat
cd win
./install.bat
```

### Distribution:

Package zip for release starting from top level of repo:

```
./build.bat
cd win
./dist.bat -v <version>
```
Now you should have win/SSHshare-`<version>`-x64-win10.tar.bz2 ready for distribution

### Installation:

1. Download the zip: `<tbd>`

2. Unzip
   ```
   uznip SSHshare-<version>-x64-win10.zip
   ```
3. Open Powershell as Administrator:
   ```
   PS C:\WINDOWS\system32> CheckNetIsolation.exe LoopbackExempt -a -n="Microsoft.Win32WebViewHost_cw5n1h2txyewy"
   ```
   Note: This is to allow hosting a webserver on localhost which is the backend of the application

4. Execute the following command:
   ```
   cd SSHshare-<version>-x64-win10
   ./install.bat
   ```