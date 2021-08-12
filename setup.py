from distutils.core import setup
from distutils.command.install import install

import pathlib, os, shutil
from os import path
from subprocess import call


# Base application info
base_rdnn = 'com.github.subhadeepjasu'
app_name = 'enigma'
app_id = base_rdnn + '.' + app_name
app_url = 'https://github.com/subhadeepjasu/' + app_name

# Setup file paths for data files
prefix = '/usr'
prefix_data = path.join(prefix, 'share')
install_path = path.join(prefix_data, app_id)
src_path = path.join(install_path, 'enigma')
emulator_path = path.join(src_path, 'emulator')
data_path = path.join(install_path, 'data')
icon_path = 'icons/hicolor'
icon_sizes = ['16','24','32','48','64','128']
icon_16 = prefix_data + '/icons/hicolor/16x16/apps'
icon_24 = prefix_data + '/icons/hicolor/24x24/apps'
icon_32 = prefix_data + '/icons/hicolor/32x32/apps'
icon_48 = prefix_data + '/icons/hicolor/48x48/apps'
icon_64 = prefix_data + '/icons/hicolor/64x64/apps'
icon_128 = prefix_data + '/icons/hicolor/128x128/apps'
icon_16_2x = prefix_data + '/icons/hicolor/16x16@2/apps'
icon_24_2x = prefix_data + '/icons/hicolor/24x24@2/apps'
icon_32_2x = prefix_data + '/icons/hicolor/32x32@2/apps'
icon_48_2x = prefix_data + '/icons/hicolor/48x48@2/apps'
icon_64_2x = prefix_data + '/icons/hicolor/64x64@2/apps'
icon_128_2x = prefix_data + '/icons/hicolor/128x128@2/apps'


# Setup install data list
install_data = [(prefix_data + '/metainfo', ['data/' + app_id + '.appdata.xml']),
                (prefix_data + '/applications', ['data/' + app_id + '.desktop']),
                (data_path,['data/Application.css']),
                (data_path,['data/Floral-Seamless-Pattern-By-Karen-Arnold.svg']),
                (src_path,['enigma' + '/constants.py']),
                (src_path,['enigma' + '/headerbar.py']),
                (src_path,['enigma' + '/keyboard.py']),
                (src_path,['enigma' + '/rotorboard.py']),
                (src_path,['enigma' + '/lampboard.py']),
                (src_path,['enigma' + '/plug.py']),
                (src_path,['enigma' + '/rotor_selector.py']),
                (src_path,['enigma' + '/scratch_pad.py']),
                (src_path,['enigma' + '/plugboard_ui.py']),
                (src_path,['enigma' + '/main.py']),
                (src_path,['enigma' + '/window.py']),
                (src_path,['enigma' + '/__init__.py']),
                (emulator_path + '/components',['enigma/emulator/components' + '/plugboard.py']),
                (emulator_path + '/components',['enigma/emulator/components' + '/reflector.py']),
                (emulator_path + '/components',['enigma/emulator/components' + '/rotor.py']),
                (emulator_path,['enigma/emulator' + '/enigma_machine.py']),
                (icon_16,['data/icons/16/' + app_id + '.svg']),
                (icon_16_2x,['data/icons/16/' + app_id + '.svg']),
                (icon_24,['data/icons/24/' + app_id + '.svg']),
                (icon_24_2x,['data/icons/24/' + app_id + '.svg']),
                (icon_32,['data/icons/32/' + app_id + '.svg']),
                (icon_32_2x,['data/icons/32/' + app_id + '.svg']),
                (icon_48,['data/icons/48/' + app_id + '.svg']),
                (icon_48_2x,['data/icons/48/' + app_id + '.svg']),
                (icon_64,['data/icons/64/' + app_id + '.svg']),
                (icon_64_2x,['data/icons/64/' + app_id + '.svg']),
                (icon_128,['data/icons/128/' + app_id + '.svg']),
                (icon_128_2x,['data/icons/128/' + app_id + '.svg'])]

# Post install commands
class PostInstall(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)

setup(
    name=app_name,  # Required
    license='GNU GPL3',
    version='0.0.2',  # Required
    url=app_url,  # Optional
    author='Subhadeep Jasu',  # Optional
    author_email='subhajasu@gmail.com',  # Optional
    scripts=[app_id],
    data_files=install_data  # Optional
)
