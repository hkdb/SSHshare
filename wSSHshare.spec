# -*- mode: python -*-

block_cipher = None


a = Analysis(['wSSHshare.py'],
             pathex=['./'],
             binaries=[
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\Atk-1.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\Gtk-3.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\GObject-2.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\GiRepository-2.0.typelib', 'gi_typelibs'),                 
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\GModule-2.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\Gdk-3.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\GdkWin32-3.0.typelib', 'gi_typelibs'),
                 (r'C:\Python27\Lib\site-packages\gnome\lib\girepository-1.0\GdkPixbuf-2.0.typelib', 'gi_typelibs'),
             ],
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