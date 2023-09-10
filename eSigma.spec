# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Y:/Coding/DiscBot/eSigma/main.py'],
    pathex=[],
    binaries=[],
    datas=[('Y:/Coding/DiscBot/eSigma/data', 'data/'), ('Y:/Coding/DiscBot/eSigma/bottoken.py', '.'), ('Y:/Coding/DiscBot/eSigma/requirements.txt', '.')],
    hiddenimports=['pynacl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='eSigma',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Y:\\Icons\\icons8-discord-50.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='eSigma',
)
