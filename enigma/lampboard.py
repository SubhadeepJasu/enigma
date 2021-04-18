#!/usr/bin/python3
'''
   Copyright 2017 Subhadeep Jasu <subhajasu@gmail.com>

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
from gi.repository import Gtk, Gdk

class Lampboard(Gtk.Grid):
    def make_ui(self):
        self.key_alphabets = "QWERTZUIOASDFGHJKPYXCVBNML"
        self.lamp_array = []
        for key in self.key_alphabets:
            lamp = Gtk.Label(key)
            lamp.get_style_context().add_class("lamp")
            lamp.props.height_request = 36
            lamp.props.width_request = 36
            self.lamp_array.append(lamp)

        self.lamp_row_upper = Gtk.Box(spacing = 2)
        self.lamp_row_middle = Gtk.Box(spacing = 2)
        self.lamp_row_lower = Gtk.Box(spacing = 2)

        key_index = 0
        while key_index < 9:
            self.lamp_row_upper.add(self.lamp_array[key_index])
            key_index+=1
        while (key_index < 17):
            self.lamp_row_middle.add(self.lamp_array[key_index])
            key_index+=1
        while (key_index < 26):
            self.lamp_row_lower.add(self.lamp_array[key_index])
            key_index+=1

        self.lamp_row_upper.set_halign(Gtk.Align.CENTER)
        self.lamp_row_middle.set_halign(Gtk.Align.CENTER)
        self.lamp_row_lower.set_halign(Gtk.Align.CENTER)

        self.lamp_row_upper.set_homogeneous(True)
        self.lamp_row_middle.set_homogeneous(True)
        self.lamp_row_lower.set_homogeneous(True)

        self.attach(self.lamp_row_upper,  0, 0, 1, 1)
        self.attach(self.lamp_row_middle, 0, 1, 1, 1)
        self.attach(self.lamp_row_lower,  0, 2, 1, 1)
        self.set_halign(Gtk.Align.FILL)
        self.set_hexpand(True)
        self.set_row_spacing(2)
        self.set_column_homogeneous(2)
        self.set_margin_top(8)
        self.get_style_context().add_class("lamp-board")
    def set_lamp_active(self, alphabet, on):
        if on:
            for lamp in self.lamp_array:
                if lamp.get_text() == alphabet:
                    lamp.get_style_context().add_class("lamp-active")
                    return None
        else:
            for lamp in self.lamp_array:
                lamp.get_style_context().remove_class("lamp-active")
        return None