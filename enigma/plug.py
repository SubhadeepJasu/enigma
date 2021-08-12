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
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

class Plug(Gtk.Button):
    def __init__(self, alphabet):
        Gtk.Button.__init__(self)
        self.get_style_context().add_class("plug-socket-button")
        self.props.height_request = 32
        self.set_image(Gtk.Image.new_from_icon_name("media-optical-symbolic", Gtk.IconSize.BUTTON))
        self._alphabet = alphabet
        self._plugged = False;

    def set_color(self, set_style, index):
        if set_style:
            self.get_style_context().add_class("plug-" + str(index))
        else:
            self.get_style_context().remove_class("plug-" + str(index))
