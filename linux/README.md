# Linux
maintained by: hkdb `<hkdb@3df.io>`

### Dependancies:

- GoLang

### Delta:

The install script will install ssh-vault into ~/.local.

### Compiling:

Execute the following if you are compiling for the first time:

```
go get
```

Execute the following scripts starting at the top level of the repo:

```
./build.sh
cd linux
./install
```

### Distribution:

Package tarball for release starting from top level of repo:

```
./build.sh
cd linux
./dist.sh -v <version>
```
Now you should have linux/SSHshare-`<version>`-x64.tar.bz2 ready for distribution

### Installation:

1. Download the tarball: `<tbd>`

2. Untar
   ```
   tar -xjvf SSHshare-<version>-x64.tar.bz2
   ```

3. Execute the following command:
   ```
   cd SSHshare-<version>-x64
   ./install
   ```
