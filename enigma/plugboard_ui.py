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

import plug as pg

class PlugBoardUI(Gtk.Overlay):
    __gsignals__ = {
        'plug_selected': (GObject.SIGNAL_RUN_FIRST, None,
                      (str,))
    }
    def make_ui(self):
        self.key_alphabets = "QWERTZUIOASDFGHJKPYXCVBNML"
        self.plug_array = []
        self.current_index = 0
        for key in self.key_alphabets:
            plug_label = Gtk.Label(key)
            plug_label.get_style_context().add_class("plug-label")
            plug_label.props.height_request = 32
            plug_label.props.width_request = 32
            plug_socket1 = Gtk.Box()
            plug_socket2 = Gtk.Box()
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

        self.plug_buttons = []
        index = 0
        for key in self.key_alphabets:
            plug = pg.Plug(key)
            plug.connect("clicked", self.plug_button_handler, key)
            self.plug_buttons.append(plug)
            index+=1

        self.button_row_upper = Gtk.Box(spacing = 27)
        self.button_row_middle = Gtk.Box(spacing = 27)
        self.button_row_lower = Gtk.Box(spacing = 27)

        key_index = 0
        while key_index < 9:
            self.button_row_upper.add(self.plug_buttons[key_index])
            key_index+=1
        while (key_index < 17):
            self.button_row_middle.add(self.plug_buttons[key_index])
            key_index+=1
        while (key_index < 26):
            self.button_row_lower.add(self.plug_buttons[key_index])
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

    def plug_button_handler(self, plug, alphabet):
        self.emit("plug_selected", alphabet)
        
    def redraw_plugs(self, plug_status):
        index = 0
        while index < len(self.plug_buttons):
            if plug_status[index]:
                self.current_index+=1
                if self.current_index == 26:
                    self.current_index = 0
                self.plug_buttons[index].get_style_context().add_class("plug-socket-button-active")
            else:
                self.plug_buttons[index].get_style_context().remove_class("plug-socket-button-active")
            index+=1

    def draw_selected_plug(self, alphabet):
        for plug in self.plug_buttons:
            if (plug._alphabet == alphabet):
                plug.get_style_context().add_class("plug-socket-button-highlight")

    def clear_plug_states(self, alpha1, alpha2):
        print(alpha1, alpha2)
        for plug in self.plug_buttons:
            if (plug._alphabet == alpha1 or plug._alphabet == alpha2):
                plug.get_style_context().remove_class("plug-socket-button-highlight")
                i = 0
                while i < 13:
                    plug.set_color(False, i)
                    i+=1

    def set_plug_pair_states(self, alpha1, alpha2):
        plug_instance1 = None
        plug_instance2 = None
        for plug in self.plug_buttons:
            if plug._alphabet == alpha1:
                plug_instance1 = plug
            if plug._alphabet == alpha2:
                plug_instance2 = plug

        plug_instance1.set_color(True, int(self.current_index/2) - 1)
        plug_instance2.set_color(True, int(self.current_index/2) - 1)
            