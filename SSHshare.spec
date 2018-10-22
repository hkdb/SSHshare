# -*- mode: python -*-

block_cipher = None

a = Analysis(['SSHshare.py'],
             pathex=['./'],
             binaries=[],
             datas=[('./header.png', '.')],
             hiddenimports=None,
             hookspath=[],
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SSHshare',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='icon.icns')

app = BUNDLE(exe,
             name='SSHshare.app',
             icon='/Users/hkdb/Development/SSHshare/icon.icns',
             bundle_identifier='com.3df.osx.sshshare',
             info_plist={
               'CFBundleName': 'SSHshare',
               'CFBundleDisplayName': 'SSHshare',
               'CFBundleGetInfoString': 'Encrypt/Decrypt Data w/ ssh-vault',
               'CFBundleIdentifier': 'com.3df.osx.sshshare',
               'CFBundleVersion': '0.1.2',
               'CFBundleShortVersionString': '0.1.2',
               'NSHumanReadableCopyright': '3DF OSI - MIT License'
              }
             )
