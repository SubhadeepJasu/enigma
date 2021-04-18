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

class PlugBoardUI(Gtk.Overlay):
    __gsignals__ = {
        'plug_pair_selected': (GObject.SIGNAL_RUN_FIRST, None,
                      (str,))
    }
    def make_ui(self):
        self.key_alphabets = "QWERTZUIOASDFGHJKPYXCVBNML"
        self.plug_array = []
        for key in self.key_alphabets:
            plug_label = Gtk.Label(key)
            plug_label.get_style_context().add_class("plug-label")
            plug_label.props.height_request = 32
            plug_label.props.width_request = 32
            plug_socket1 = Gtk.Label("")
            plug_socket2 = Gtk.Label("")
            plug_socket1.get_style_context().add_class("plug-socket")
            plug_socket1.props.height_request = 21
            plug_socket1.props.width_request = 21
            plug_socket2.get_style_context().add_class("plug-socket")
            plug_socket2.props.height_request = 21
            plug_socket2.props.width_request = 21
            plug = Gtk.Grid()
            plug.set_row_spacing(1)
            plug.attach(plug_label, 0, 0, 1, 2)
            plug.attach(plug_socket1, 1, 0, 1, 1)
            plug.attach(plug_socket2, 1, 1, 1, 1)
            self.plug_array.append(plug)

        self.plug_row_upper = Gtk.Box(spacing = 4)
        self.plug_row_middle = Gtk.Box(spacing = 4)
        self.plug_row_lower = Gtk.Box(spacing = 4)

        key_index = 0
        while key_index < 9:
            self.plug_row_upper.add(self.plug_array[key_index])
            key_index+=1
        while (key_index < 17):
            self.plug_row_middle.add(self.plug_array[key_index])
            key_index+=1
        while (key_index < 26):
            self.plug_row_lower.add(self.plug_array[key_index])
            key_index+=1

        self.plug_row_upper.set_halign(Gtk.Align.CENTER)
        self.plug_row_middle.set_halign(Gtk.Align.CENTER)
        self.plug_row_lower.set_halign(Gtk.Align.CENTER)

        self.plug_row_upper.set_homogeneous(True)
        self.plug_row_middle.set_homogeneous(True)
        self.plug_row_lower.set_homogeneous(True)
        
        plug_board_layout_grid = Gtk.Grid()
        plug_board_layout_grid.attach(self.plug_row_upper, 0, 0, 1, 1)
        plug_board_layout_grid.attach(self.plug_row_middle, 0, 1, 1, 1)
        plug_board_layout_grid.attach(self.plug_row_lower, 0, 2, 1, 1)

        self.plug_button = []
        index = 0
        for key in self.key_alphabets:
            plug = Gtk.Button.new_from_icon_name("user-idle", Gtk.IconSize.BUTTON)
            plug.get_style_context().add_class("plug-socket-button")
            plug.props.height_request = 32
            plug.connect("clicked", self.plug_button_handler, key, index)
            self.plug_button.append(plug)
            index+=1

        self.button_row_upper = Gtk.Box(spacing = 27)
        self.button_row_middle = Gtk.Box(spacing = 27)
        self.button_row_lower = Gtk.Box(spacing = 27)

        key_index = 0
        while key_index < 9:
            self.button_row_upper.add(self.plug_button[key_index])
            key_index+=1
        while (key_index < 17):
            self.button_row_middle.add(self.plug_button[key_index])
            key_index+=1
        while (key_index < 26):
            self.button_row_lower.add(self.plug_button[key_index])
            key_index+=1

        self.button_row_upper.set_halign(Gtk.Align.CENTER)
        self.button_row_middle.set_halign(Gtk.Align.CENTER)
        self.button_row_lower.set_halign(Gtk.Align.CENTER)

        self.button_row_upper.set_homogeneous(True)
        self.button_row_middle.set_homogeneous(True)
        self.button_row_lower.set_homogeneous(True)

        self.button_row_upper.set_margin_left(33)
        self.button_row_middle.set_margin_left(33)
        self.button_row_lower.set_margin_left(33)

        self.button_row_upper.props.height_request = 43
        self.button_row_middle.props.height_request = 43
        self.button_row_lower.props.height_request = 43
        
        plug_button_socket_grid = Gtk.Grid()
        plug_button_socket_grid.attach(self.button_row_upper, 0, 0, 1, 1)
        plug_button_socket_grid.attach(self.button_row_middle, 0, 1, 1, 1)
        plug_button_socket_grid.attach(self.button_row_lower, 0, 2, 1, 1)

        
        plug_board_layout_grid.set_halign(Gtk.Align.CENTER)
        plug_button_socket_grid.set_halign(Gtk.Align.CENTER)
        self.add_overlay(plug_board_layout_grid)
        self.add_overlay(plug_button_socket_grid)

    _connecting_alphabet = ""
    def plug_button_handler(self, plug, alphabet, index):
        if len(self._connecting_alphabet) == 0:
            self._connecting_alphabet += alphabet
        else:
            connected_alpha = alphabet + self._connecting_alphabet
            self._connecting_alphabet = ""
            self.emit("plug_pair_selected", connected_alpha)
        

    def redraw_plugs(self, plug_status):
        index = 0
        while index < len(self.plug_button):
            if plug_status[index]:
                self.plug_button[index].get_style_context().add_class("plug-socket-button-active")
            else:
                self.plug_button[index].get_style_context().remove_class("plug-socket-button-active")
            index+=1