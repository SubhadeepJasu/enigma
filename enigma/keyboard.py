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

class Keyboard(Gtk.Grid):   
    __gsignals__ = {
        'key_button_pressed': (GObject.SIGNAL_RUN_FIRST, None,
                      (str,)) ,
        'key_button_released': (GObject.SIGNAL_RUN_FIRST, None,
                      (str,)) 
    }
    def make_ui(self):
        self.key_alphabets = "QWERTZUIOASDFGHJKPYXCVBNML"
        self.key_array = []
        for key in self.key_alphabets:
            btn = Gtk.Button.new_with_label(key)
            btn.get_style_context().add_class("keyboard-button")
            btn.props.height_request = 40
            btn.props.width_request = 40
            btn.connect("pressed", self._send_key, key)
            btn.connect("released", self._send_key_release, key)
            self.key_array.append(btn)

        self.key_row_upper = Gtk.Box(spacing = 4)
        self.key_row_middle = Gtk.Box(spacing = 4)
        self.key_row_lower = Gtk.Box(spacing = 4)

        key_index = 0
        while key_index < 9:
            self.key_row_upper.add(self.key_array[key_index])
            key_index+=1
        while (key_index < 17):
            self.key_row_middle.add(self.key_array[key_index])
            key_index+=1
        while (key_index < 26):
            self.key_row_lower.add(self.key_array[key_index])
            key_index+=1

        self.key_row_upper.set_halign(Gtk.Align.CENTER)
        self.key_row_middle.set_halign(Gtk.Align.CENTER)
        self.key_row_lower.set_halign(Gtk.Align.CENTER)

        self.key_row_upper.set_homogeneous(True)
        self.key_row_middle.set_homogeneous(True)
        self.key_row_lower.set_homogeneous(True)

        self.attach(self.key_row_upper,  0, 0, 1, 1)
        self.attach(self.key_row_middle, 0, 1, 1, 1)
        self.attach(self.key_row_lower,  0, 2, 1, 1)
        self.set_halign(Gtk.Align.CENTER)
        self.set_hexpand(True)
        self.set_row_spacing(4)
        self.set_margin_top(8)
        self.set_margin_bottom(8)

    def _send_key(self, button, key_val):
        self.emit("key_button_pressed", key_val)

    def _send_key_release(self, button, key_val):
        self.emit("key_button_released", key_val)
