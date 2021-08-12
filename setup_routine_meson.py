#!/usr/bin/python3

import glob, os 
from distutils.core import setup
from subprocess import call

install_data = [('bin/enigma/data',['data/Application.css']),
                ('bin/enigma/data',['data/Floral-Seamless-Pattern-By-Karen-Arnold.svg']),
                ('bin/enigma/emulator/components',['enigma/emulator/components/plugboard.py']),
                ('bin/enigma/emulator/components',['enigma/emulator/components/reflector.py']),
                ('bin/enigma/emulator/components',['enigma/emulator/components/rotor.py']),
                ('bin/enigma/emulator',['enigma/emulator/enigma_machine.py']),
                ('bin/enigma',['enigma/constants.py']),
                ('bin/enigma',['enigma/headerbar.py']),
                ('bin/enigma',['enigma/keyboard.py']),
                ('bin/enigma',['enigma/rotorboard.py']),
                ('bin/enigma',['enigma/lampboard.py']),
                ('bin/enigma',['enigma/plug.py']),
                ('bin/enigma',['enigma/rotor_selector.py']),
                ('bin/enigma',['enigma/scratch_pad.py']),
                ('bin/enigma',['enigma/plugboard_ui.py']),
                ('bin/enigma',['enigma/main.py']),
                ('bin/enigma',['enigma/window.py']),
                ('bin/enigma',['enigma/__init__.py'])]

setup(  name='Enigma',
        version='0.0.2',
        author='Subhadeep Jasu',
        description='An Enigma Machine simulator',
        url='https://github.com/subhadeepjasu/enigma',
        license='GNU GPL3',
        scripts=['com.github.subhadeepjasu.enigma'],
        packages=['enigma'],
        data_files=install_data)

