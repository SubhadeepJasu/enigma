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
import constants as cn
import headerbar as hb
import keyboard  as kb
import lampboard as lb
import rotorboard as rb
import plugboard_ui as pb
import rotor_selector as rs
import scratch_pad as sp
import emulator.enigma_machine as em

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Window(Gtk.Window):
    settings = Gtk.Settings.get_default()
    def __init__(self):
        Gtk.Window.__init__(self, title=cn.App.application_name)

        self.settings.set_property("gtk-application-prefer-dark-theme", True)

        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        self.rotorboard = rb.Rotorboard()
        self.rotorboard.set_margin_left(8)
        self.rotorboard.make_ui()

        self.lampboard = lb.Lampboard()
        self.lampboard.make_ui()

        self.keyboard = kb.Keyboard()
        self.keyboard.make_ui()

        self.plugboard = pb.PlugBoardUI()
        self.plugboard.make_ui()
        self.plugboard.set_margin_top(4)
        self.plugboard.props.height_request = 150
        self.plugboard.connect("plug_selected", self.remap_plugboard)

        self.show_plug_board_button = Gtk.Button.new_with_label ("Toggle Plugboard")
        self.plugboard_revealer = Gtk.Revealer()
        self.plugboard_revealer.add(self.plugboard)

        self.show_plug_board_button.connect("clicked", self.revealer_handler)

        self._create_enigma_machine()
        self.rotor_selector = rs.RotorSelector(self.enigma_machine.get_all_rotor_names(), self.rotor_selection_handler)


        self.scratchpad = sp.ScratchPad()
        self.scratchpad.set_margin_top(8)
        self.scratchpad.set_margin_right(8)
        self.scratchpad.connect("batch_encrypt", self._batch_compile_handler)

        main_grid = Gtk.Grid()
        main_grid.attach(self.rotorboard, 0, 0, 1, 1)
        main_grid.attach(self.rotor_selector, 1, 0, 1, 1)
        main_grid.attach(self.scratchpad, 2, 0, 1, 1)
        main_grid.attach(self.lampboard, 0, 1, 3, 1)
        main_grid.attach(self.keyboard, 0, 2, 3, 1)
        main_grid.attach(self.show_plug_board_button, 0, 3, 3, 1)
        main_grid.attach(self.plugboard_revealer, 0, 4, 3, 1)
        main_grid.set_column_spacing(8)

        self.add(main_grid)

        self.keyboard.connect("key_button_pressed", self._press_keys)
        self.keyboard.connect("key_button_released", self._release_keys)

        self.rotorboard.connect("manual_rotate1", self._manual_rotate1)
        self.rotorboard.connect("manual_rotate2", self._manual_rotate2)
        self.rotorboard.connect("manual_rotate3", self._manual_rotate3)
    
    def revealer_handler(self, button):
        self.plugboard_revealer.props.reveal_child = not self.plugboard_revealer.props.reveal_child

    def rotor_selection_handler(self, rotors):
        self.enigma_machine.connect_rotor(1, self.enigma_machine.get_rotor_by_name(rotors[0]), self._rotor_callback1)
        self.enigma_machine.connect_rotor(2, self.enigma_machine.get_rotor_by_name(rotors[1]), self._rotor_callback2)
        self.enigma_machine.connect_rotor(3, self.enigma_machine.get_rotor_by_name(rotors[2]), self._rotor_callback3)

    def _create_enigma_machine(self):
        self.enigma_machine = em.EnigmaMachine()
        self.enigma_machine.connect_rotor(1, self.enigma_machine.get_rotor_by_name("IC"), self._rotor_callback1)
        self.enigma_machine.connect_rotor(2, self.enigma_machine.get_rotor_by_name("IIC"), self._rotor_callback2)
        self.enigma_machine.connect_rotor(3, self.enigma_machine.get_rotor_by_name("IIIC"), self._rotor_callback3)
        self.enigma_machine.set_rotor_config(0,0,0)

    def remap_plugboard (self, plugboard, alphabet):
        self.enigma_machine.plug_plugboard(alphabet, self.plugboard_selection_handler)
        
    def plugboard_selection_handler(self, function, alpha1, alpha2):
        if function == "select_await":
            self.plugboard.draw_selected_plug(alpha1)
        active_plugs = self.enigma_machine.get_active_plugs()
        self.plugboard.redraw_plugs(active_plugs)
        if function == "select_complete":
            self.plugboard.clear_plug_states(alpha1, alpha2)
            self.plugboard.set_plug_pair_states(alpha1, alpha2)
        if function == "clear":
            self.plugboard.clear_plug_states(alpha1, alpha2)

    def _press_keys(self, keyboard, key_val):
        new_key = self.enigma_machine.type_alphabet(key_val)
        self.lampboard.set_lamp_active(new_key, True)
        self.scratchpad.append_to_text(new_key)

    def _release_keys(self, keyboard, key_val):
        self.lampboard.set_lamp_active(key_val, False)

    def _rotor_callback1(self, direction):
        alphabet = self.enigma_machine.get_rotor1_alphabet()
        self.rotorboard.set_rotor_label3(alphabet)
        if direction:
            self.rotorboard.rotate_rotor3_down()
        else:
            self.rotorboard.rotate_rotor3_up()
    
    def _rotor_callback2(self, direction):
        alphabet = self.enigma_machine.get_rotor2_alphabet()
        self.rotorboard.set_rotor_label2(alphabet)
        if direction:
            self.rotorboard.rotate_rotor2_down()
        else:
            self.rotorboard.rotate_rotor2_up()
    
    def _rotor_callback3(self, direction):
        alphabet = self.enigma_machine.get_rotor3_alphabet()
        self.rotorboard.set_rotor_label1(alphabet)
        if direction:
            self.rotorboard.rotate_rotor1_down()
        else:
            self.rotorboard.rotate_rotor1_up()

    def _manual_rotate1(self, rotatorboard, direction):
        self.enigma_machine.rotate_rotor_1(direction)
    
    def _manual_rotate2(self, rotatorboard, direction):
        self.enigma_machine.rotate_rotor_2(direction)
    
    def _manual_rotate3(self, rotatorboard, direction):
        self.enigma_machine.rotate_rotor_3(direction)


    def _batch_compile_handler(self, scratchpad_obj, text):
        print(text)
        for alphabet in text:
            cypher = self.enigma_machine.type_alphabet(alphabet)
            self.scratchpad.append_to_text(cypher)
