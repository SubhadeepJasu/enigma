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

import gi, re
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

class ScratchPad(Gtk.Grid):
    __gsignals__ = {
        'batch_encrypt': (GObject.SIGNAL_RUN_FIRST, None,
                      (str,))
    }
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.get_style_context().add_class("scratch-pad")
        self._text_area = Gtk.TextView()
        self._text_buffer = self._text_area.get_buffer()
        self._text_area.props.width_request = 200
        self._text_area.props.height_request = 140
        self._text_area.set_size_request(200,140)
        self.set_size_request(200,140)
        self._text_area.props.monospace = True
        self._text_area.set_wrap_mode(Gtk.WrapMode.CHAR)
        self._clear_button = Gtk.Button.new_from_icon_name("edit-clear", Gtk.IconSize.BUTTON)
        self._clear_button.connect("clicked", self._clear_text_handler)
        self._batch_encrypt_button = Gtk.Button.new_from_icon_name("media-playback-start", Gtk.IconSize.BUTTON)
        self._batch_encrypt_button.connect("clicked", self._batch_compile_handler)
        scrolled_window = Gtk.ScrolledWindow(None, None)
        scrolled_window.add_with_viewport(self._text_area)
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.attach(scrolled_window, 0, 0, 2, 1)
        self.attach(self._batch_encrypt_button, 0, 1, 1, 1)
        self.attach(self._clear_button, 1, 1, 1, 1)

    def append_to_text(self, alphabet):
        self._text_buffer.insert_at_cursor(alphabet, 1)
    
    def _batch_compile_handler(self, button):
        self._text_buffer.set_text(self._process_text(self._text_buffer.get_text(self._text_buffer.get_start_iter(), self._text_buffer.get_end_iter(), False)))
        final_text = self._text_buffer.get_text(self._text_buffer.get_start_iter(), self._text_buffer.get_end_iter(), False)
        self._text_buffer.insert_at_cursor('\n', 1)
        self.emit("batch_encrypt", final_text)

    def _clear_text_handler(self, button):
        self._text_buffer.set_text("")

    def _process_text(self, text):
        regex = re.compile('[^a-zA-Z]')
        replaced = regex.sub('', text)
        return replaced.upper()

