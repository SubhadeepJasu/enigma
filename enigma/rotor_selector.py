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
from gi.repository import Gtk, Gdk, GObject

class RotorSelector(Gtk.Grid):
    def  __init__(self, rotors, callback):
        Gtk.Grid.__init__(self)
        self._name_array = rotors
        self._checkbox_array = []
        self._callback = callback
        i = 1
        rotor_header = Gtk.Label("Rotor Selection")
        rotor_header.set_halign(Gtk.Align.START)
        rotor_header.get_style_context().add_class("h4")
        self.attach(rotor_header, 0, 0, 3, 1)
        for rotor in rotors:
            checkbutton = Gtk.CheckButton.new_with_label(rotor)
            self._checkbox_array.append(checkbutton)
            checkbutton.connect("toggled", self._checkbox_handler, rotor)
            up_arrow = Gtk.Button.new_from_icon_name("go-up-symbolic", Gtk.IconSize.MENU)
            up_arrow.connect("clicked", self._move_rotor, i-1, True)
            down_arrow = Gtk.Button.new_from_icon_name("go-down-symbolic", Gtk.IconSize.MENU)
            down_arrow.connect("clicked", self._move_rotor, i-1, False)
            self.attach(checkbutton, 0, i, 1, 1)
            self.attach(up_arrow, 1, i, 1, 1)
            self.attach(down_arrow, 2, i, 1, 1)
            i+=1
        self._active_count = 0
        self._set_defaults()

    def _place_rotors(self):
        for rotor in self._checkbox_array:
            self.remove (rotor)
        i = 1
        for rotor in self._checkbox_array:
            self.attach(rotor, 0, i, 1, 1)
            i+=1
        if (self._active_count == 3):
            self._callback(self._get_list_of_active_rotors())
    
    def _checkbox_handler(self, button, name):
        self._count_active_rotors()
        if (self._active_count > 3):
            self._disable_one_rotor()

    def _count_active_rotors(self):
        self._active_count = 0
        for button in self._checkbox_array:
            if button.props.active:
                self._active_count += 1

    def _disable_one_rotor(self):
        for button in self._checkbox_array:
            if button.props.active:
                button.props.active = False
                break

    def _get_list_of_active_rotors(self):
        names = []
        i = 0
        for button in self._checkbox_array:
            if button.props.active:
                names.append(self._name_array[i])
            i+=1
        return names

    def _move_rotor(self, button, index, direction):
        if direction:
            if index <= 0:
                return False
            else:
                _temp_checkbox = self._checkbox_array[index]
                self._checkbox_array[index] = self._checkbox_array[index - 1]
                self._checkbox_array[index - 1] = _temp_checkbox

                _temp_name = self._name_array[index]
                self._name_array[index] = self._name_array[index - 1]
                self._name_array[index - 1] = _temp_name
        else:
            if index >= len(self._name_array) - 1:
                return False
            else:
                _temp_checkbox = self._checkbox_array[index]
                self._checkbox_array[index] = self._checkbox_array[index + 1]
                self._checkbox_array[index + 1] = _temp_checkbox

                _temp_name = self._name_array[index]
                self._name_array[index] = self._name_array[index + 1]
                self._name_array[index + 1] = _temp_name
        self._place_rotors()

    def _set_defaults(self):
        self._checkbox_array[0].props.active = True
        self._checkbox_array[1].props.active = True
        self._checkbox_array[2].props.active = True