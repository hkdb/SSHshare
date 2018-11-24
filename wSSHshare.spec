# -*- mode: python -*-

block_cipher = None


a = Analysis(['SSHshare.py'],
             pathex=['./'],
             binaries=[],
             datas=[('./header.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=False,
          name='SSHshare',
          debug=True,
          strip=False,
          upx=True,
          console=True,
          icon='icon.ico')