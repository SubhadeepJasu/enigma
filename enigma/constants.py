#!/usr/bin/python3
'''
   Copyright 2020-2021 Subhadeep Jasu <subhajasu@gmail.com>

   This file is part of Enigma.

    Enigma is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Enigma is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Enigma.  If not, see <http://www.gnu.org/licenses/>.
'''
import gi
import os
import locale
import gettext
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

try:
    current_locale, encoding = locale.getdefaultlocale()
    locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    translate = gettext.translation ("enigma", locale_path, [current_locale] )
    _ = translate.gettext
except FileNotFoundError:
    _ = str

class App:
    application_shortname = "enigma"
    application_id = "com.github.subhadeepjasu.enigma"
    application_name = "Enigma"
    application_description = _('Enigma Machine Simulator')
    application_version ="1.1"
    app_years = "2017-2018"
    main_url = "https://git.mirko.pm/brombinmirko/Enigma"
    bug_url = "https://git.mirko.pm/brombinmirko/Enigma/issues/labels/bug"
    help_url = "https://git.mirko.pm/brombinmirko/Enigma/issues"
    translate_url = "https://git.mirko.pm/brombinmirko/Enigma/blob/master/CONTRIBUTING.md"
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0

class Colors:
    primary_color = "rgba(100, 85, 82, 1)"
    primary_text_color = "#EEEDEC"
    primary_text_shadow_color = "#53433F"
