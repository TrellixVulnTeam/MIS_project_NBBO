# -*- mode: python -*-

block_cipher = None


a = Analysis(['D9_xls.py'],
             pathex=['C:\\Users\\�ü��̵ĸ���ʦ\\Desktop\\mis��Ŀ\\����Ŀ\\15.2���ڱ�Ҷ˹�㷨�������û����õȼ�����������+�ĵ���'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='D9_xls',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
