# macOS Installation - How-To

### Step 1:

Install HomeBrew via Terminal.app if you haven't already:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Step 2:

Install ssh-vault:

```
brew install ssh-vault
```

### Step 3:

Download the latest binary [ZIP](https://github.com/hkdb/SSHshare/raw/develop/macos/SSHshare.zip)

### Step 4:

Unzip & copy App Bundle into your /Applications Folder

### Step 5:

Allow Apps Downloaded from Anywhere

![Allow](https://camo.githubusercontent.com/9db180df505d958012e9c1eb285a0e8b458b47e9/68747470733a2f2f6f73692e3364662e696f2f77702d636f6e74656e742f75706c6f6164732f323031382f30352f4d6163536563757269747953657474696e67732e706e67)

If the option Anywhere is missing, click on the lock icon to unlock the settings:

![Missing Anywhere Option](https://camo.githubusercontent.com/3ba5ed1c649280e2560a452f9cace345cd5a78b2/68747470733a2f2f6f73692e3364662e696f2f77702d636f6e74656e742f75706c6f6164732f323031382f30362f6e6f646576656c6f7065726f7074696f6e2e706e67)

If it still does not show, then execute the following command in the terminal:

```
sudo spctl --master-disable
```

To lock the settings back up, execute the following command in the terminal:

```
sudo spectl --master-enable
```

Enjoy!