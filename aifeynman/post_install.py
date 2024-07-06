#!/usr/bin/env python3
import os
import stat

# List of scripts to make executable
scripts = [
    'feynman_sr1',
    'feynman_sr2',
    'feynman_sr3',
    'feynman_sr_mdl_mult',
    'feynman_sr_mdl_plus',
    'feynman_sr_mdl4',
    'feynman_sr_mdl5'
]

bindir = os.environ.get('MESON_INSTALL_DESTDIR_PREFIX', '') + os.environ.get('bindir')

print('hi')

for script in scripts:
    script_path = os.path.join(bindir, script)
    if os.path.exists(script_path):
        st = os.stat(script_path)
        os.chmod(script_path, st.st_mode | stat.S_IEXEC)