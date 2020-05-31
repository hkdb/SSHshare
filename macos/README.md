# MacOS (Darwin)
maintained by: hkdb `<hkdb@3df.io>`

![SSHshare](../SSHshare-icon.png)

### Dependancies:

- GoLang
- Catalina

### Delta:

The Mac binaries include ssh-vault already so ssh-vault does not need to be install separately.

### Compiling:

Execute the following if you are compiling for the first time:

```
go get
```

Execute the following scripts starting at the top level of the repo:

```
./build.sh
cd macos/
./dist
./install
```

It's now compiled and installed on your system. 

### Installation:

1. Download Mac Binary: SSHshare-[version]-x64-MacOS.dmg

2. Double Click the downloaded dmg

3. Move to "/Applications" directory.