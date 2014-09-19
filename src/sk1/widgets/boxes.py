# -*- coding: utf-8 -*-
#
#	Copyright (C) 2014 by Igor E. Novikov
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

class HBox(Gtk.HBox):

	def __init__(self):
		Gtk.HBox.__init__(self)

	def pack_start(self, child, expand=False, fill=False, padding=0):
		Gtk.HBox.pack_start(self, child, expand, fill, padding)

	def pack_end(self, child, expand=False, fill=False, padding=0):
		Gtk.HBox.pack_end(child, expand, fill, padding)

	def remove(self, child):
		Gtk.HBox.remove(child)

class VBox(Gtk.VBox):

	def __init__(self):
		Gtk.VBox.__init__(self)

	def pack_start(self, child, expand=False, fill=False, padding=0):
		Gtk.VBox.pack_start(self, child, expand, fill, padding)

	def pack_end(self, child, expand=False, fill=False, padding=0):
		Gtk.VBox.pack_end(child, expand, fill, padding)

	def remove(self, child):
		Gtk.VBox.remove(child)

class HidableArea(VBox):

	visibility = False

	def __init__(self):
		VBox.__init__(self)

		self.vbox = VBox()
		self.vbox2 = VBox()
		self.pack_start(self.vbox2, True, True, 0)

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.remove(self.vbox2)
			self.pack_start(self.box, True, True, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.vbox)
			self.pack_start(self.vbox2, True, True, 0)
			self.visibility = False
			self.show_all()

class HidableHBox(HBox):

	visibility = False

	def __init__(self):
		HBox.__init__(self)

		self.box = HBox()

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.pack_start(self.box, False, False, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.box)
			self.visibility = False

class HidableVBox(VBox):

	visibility = False

	def __init__(self):
		VBox.__init__(self)

		self.box = VBox()

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.pack_start(self.box, False, False, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.box)
			self.visibility = False
