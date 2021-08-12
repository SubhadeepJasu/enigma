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

from threading import Thread, Event
import time

class Rotorboard(Gtk.Grid):
    __gsignals__ = {
        'manual_rotate1': (GObject.SIGNAL_RUN_FIRST, None,
                      (bool,)) ,
        'manual_rotate2': (GObject.SIGNAL_RUN_FIRST, None,
                      (bool,)) ,
        'manual_rotate3': (GObject.SIGNAL_RUN_FIRST, None,
                      (bool,)) 
    }
    stop_event = Event()
    def make_ui(self):
        main_box = Gtk.Grid()
        main_box.set_row_spacing(4)
        main_box.set_column_spacing(4)

        self._rotor1_label = Gtk.Label("A")
        self._rotor1_label.get_style_context().add_class("rotor-label")
        self._rotor1_label.props.height_request = 32
        self._rotor1_label.set_valign(Gtk.Align.CENTER)
        self._rotor2_label = Gtk.Label("A")
        self._rotor2_label.get_style_context().add_class("rotor-label")
        self._rotor2_label.props.height_request = 32
        self._rotor2_label.set_valign(Gtk.Align.CENTER)
        self._rotor3_label = Gtk.Label("A")
        self._rotor3_label.get_style_context().add_class("rotor-label")
        self._rotor3_label.props.height_request = 32
        self._rotor3_label.set_valign(Gtk.Align.CENTER)

        rotor1_rotate_up_button = Gtk.Button.new_from_icon_name("go-up-symbolic", Gtk.IconSize.BUTTON)
        rotor1_rotate_down_button = Gtk.Button.new_from_icon_name("go-down-symbolic", Gtk.IconSize.BUTTON)
        rotor2_rotate_up_button = Gtk.Button.new_from_icon_name("go-up-symbolic", Gtk.IconSize.BUTTON)
        rotor2_rotate_down_button = Gtk.Button.new_from_icon_name("go-down-symbolic", Gtk.IconSize.BUTTON)
        rotor3_rotate_up_button = Gtk.Button.new_from_icon_name("go-up-symbolic", Gtk.IconSize.BUTTON)
        rotor3_rotate_down_button = Gtk.Button.new_from_icon_name("go-down-symbolic", Gtk.IconSize.BUTTON)

        self._rotor1_visual = Gtk.Label("")
        self._rotor1_visual.get_style_context().add_class("rotor-visual")
        self._rotor1_visual.props.height_request = 158
        self._rotor1_visual.props.width_request = 6
        self._rotor2_visual = Gtk.Label("")
        self._rotor2_visual.get_style_context().add_class("rotor-visual")
        self._rotor2_visual.props.height_request = 158
        self._rotor2_visual.props.width_request = 6
        self._rotor3_visual = Gtk.Label("")
        self._rotor3_visual.get_style_context().add_class("rotor-visual")
        self._rotor3_visual.props.height_request = 158
        self._rotor3_visual.props.width_request = 6

        main_box.attach(rotor1_rotate_up_button, 0, 0, 1, 1)
        main_box.attach(self._rotor1_label, 0, 1, 1, 1)
        main_box.attach(rotor1_rotate_down_button, 0, 2, 1, 1)
        main_box.attach(self._rotor1_visual, 1, 0, 1, 3)
        main_box.attach(rotor2_rotate_up_button, 2, 0, 1, 1)
        main_box.attach(self._rotor2_label, 2, 1, 1, 1)
        main_box.attach(rotor2_rotate_down_button, 2, 2, 1, 1)
        main_box.attach(self._rotor2_visual, 3, 0, 1, 3)
        main_box.attach(rotor3_rotate_up_button, 4, 0, 1, 1)
        main_box.attach(self._rotor3_label, 4, 1, 1, 1)
        main_box.attach(rotor3_rotate_down_button, 4, 2, 1, 1)
        main_box.attach(self._rotor3_visual, 5, 0, 1, 3)

        self.attach(main_box, 0, 0, 1, 1)
        self.set_halign(Gtk.Align.CENTER)
        self.set_margin_top(8)
        self.set_margin_bottom(8)

        rotor1_rotate_up_button.connect("clicked", self._rotor1_up_button_handler)
        rotor1_rotate_down_button.connect("clicked", self._rotor1_down_button_handler)
        rotor2_rotate_up_button.connect("clicked", self._rotor2_up_button_handler)
        rotor2_rotate_down_button.connect("clicked", self._rotor2_down_button_handler)
        rotor3_rotate_up_button.connect("clicked", self._rotor3_up_button_handler)
        rotor3_rotate_down_button.connect("clicked", self._rotor3_down_button_handler)

    def _rotor1_up_button_handler(self, button):
        self.emit("manual_rotate3", False)
        
    def _rotor1_down_button_handler(self, button):
        self.emit("manual_rotate3", True)

    def _rotor2_up_button_handler(self, button):
        self.emit("manual_rotate2", False)
        
    def _rotor2_down_button_handler(self, button):
        self.emit("manual_rotate2", True)
    
    def _rotor3_up_button_handler(self, button):
        self.emit("manual_rotate1", False)
        
    def _rotor3_down_button_handler(self, button):
        self.emit("manual_rotate1", True)
    
    def rotate_rotor1_up(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor1_visual.get_style_context().add_class("rotor-rotate-up")
        wait_thread.start()

    def rotate_rotor1_down(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor1_visual.get_style_context().add_class("rotor-rotate-down")
        wait_thread.start()
    
    def rotate_rotor2_up(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor2_visual.get_style_context().add_class("rotor-rotate-up")
        wait_thread.start()

    def rotate_rotor2_down(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor2_visual.get_style_context().add_class("rotor-rotate-down")
        wait_thread.start()
    
    def rotate_rotor3_up(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor3_visual.get_style_context().add_class("rotor-rotate-up")
        wait_thread.start()

    def rotate_rotor3_down(self):
        wait_thread = Thread(target=self._timeout_wait)
        self._rotor3_visual.get_style_context().add_class("rotor-rotate-down")
        wait_thread.start()

    def rotate_perpetual_down(self, on):
        if on:
            self._rotor3_visual.get_style_context().add_class("rotor-rotate-down")
        else:
            self._rotor3_visual.get_style_context().remove_class("rotor-rotate-down")

    def _timeout_wait(self):
        time.sleep(0.3)
        if self._rotor1_visual.get_style_context().has_class("rotor-rotate-up"):
            self._rotor1_visual.get_style_context().remove_class("rotor-rotate-up")
        if self._rotor1_visual.get_style_context().has_class("rotor-rotate-down"):
            self._rotor1_visual.get_style_context().remove_class("rotor-rotate-down")
        if self._rotor2_visual.get_style_context().has_class("rotor-rotate-up"):
            self._rotor2_visual.get_style_context().remove_class("rotor-rotate-up")
        if self._rotor2_visual.get_style_context().has_class("rotor-rotate-down"):
            self._rotor2_visual.get_style_context().remove_class("rotor-rotate-down")
        if self._rotor3_visual.get_style_context().has_class("rotor-rotate-up"):
            self._rotor3_visual.get_style_context().remove_class("rotor-rotate-up")
        if self._rotor3_visual.get_style_context().has_class("rotor-rotate-down"):
            self._rotor3_visual.get_style_context().remove_class("rotor-rotate-down")
        time.sleep(0.1)

    def set_rotor_label1(self, alphabet):
        self._rotor1_label.set_text(alphabet)
    
    def set_rotor_label2(self, alphabet):
        self._rotor2_label.set_text(alphabet)

    def set_rotor_label3(self, alphabet):
        self._rotor3_label.set_text(alphabet)
