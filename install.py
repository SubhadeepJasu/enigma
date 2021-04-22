#!/usr/bin/python3

import os, sys
from os import path, environ
import subprocess

setup_path = (os.path.dirname(os.path.abspath(sys.argv[0])))
os.chdir(setup_path)
os.system('python3 setup_routine_meson.py install')


prefix = environ.get('MESON_INSTALL_PREFIX', '/usr/local')
schemadir = path.join(environ['MESON_INSTALL_PREFIX'], 'share', 'glib-2.0', 'schemas')
datadir = path.join(prefix, 'share')
desktop_database_dir = path.join(datadir, 'applications')

if not environ.get('DESTDIR'):
    print('Compiling gsettings schemas…')
    subprocess.call(['glib-compile-schemas', schemadir])
    print('Updating desktop database…')
    subprocess.call(['update-desktop-database', '-q', desktop_database_dir])
    print('Updating icon cache…')
    subprocess.call(['gtk-update-icon-cache', '-qtf', path.join(datadir, 'icons', 'hicolor')])