# -*- mode: python -*-

block_cipher = None


a = Analysis(['App.py'],
             pathex=['D:\\MIS_project_2019_07_19\\��ѧ��ʾ���_Դ�뼰����ĵ�\\Դ����\\17.1ATM�Ŷ�ģ��ϵͳ\\ATM-Queue-Simulation\\ATM-Queue-Simulation'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
