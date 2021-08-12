# Project name, programming language and version
project (
    'com.github.subhadeepjasu.enigma',
    version: '1.0.1',
)

# GNOME module
gnome = import ('gnome')

# Translation module
i18n = import ('i18n')

# Python module
py_mod = import('python')

message('Looking for dependencies')
py_installation = py_mod.find_installation('python3')
if not py_installation.found()
    error('No valid python3 binary found')
else
    message('Found python3 binary')
endif


dependency ('granite')
dependency ('gtk+-3.0')
dependency ('glib-2.0')
dependency ('gobject-2.0')


subdir ('data')
subdir ('po')

meson.add_install_script ('install.py')
