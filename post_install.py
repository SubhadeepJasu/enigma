#!/usr/bin/env python3

from os import environ, path
from subprocess import call

prefix = '/usr'
datadir = path.join(prefix, 'share')

print('Updating icon cache...')
call(['gtk-update-icon-cache', '-qtf', path.join(datadir, 'icons', 'hicolor')])