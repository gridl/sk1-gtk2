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

	def __init__(self):Gtk.HBox.__init__(self)

class VBox(Gtk.VBox):

	def __init__(self):Gtk.VBox.__init__(self)

class HidableArea(Gtk.VBox):

	visibility = False

	def __init__(self):
		Gtk.VBox.__init__(self)

		self.box = Gtk.VBox()
		self.box2 = Gtk.VBox()
		self.pack_start(self.box2, True, True, 0)

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.remove(self.box2)
			self.pack_start(self.box, True, True, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.box)
			self.pack_start(self.box2, True, True, 0)
			self.visibility = False
			self.show_all()

class HidableHBox(Gtk.HBox):

	visibility = False

	def __init__(self):
		Gtk.HBox.__init__(self)

		self.box = Gtk.HBox()

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.pack_start(self.box, False, False, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.box)
			self.visibility = False

class HidableVBox(Gtk.VBox):

	visibility = False

	def __init__(self):
		Gtk.VBox.__init__(self)

		self.box = Gtk.VBox()

	def set_visible(self, visible):
		if visible and not self.visibility:
			self.pack_start(self.box, False, False, 0)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			self.remove(self.box)
			self.visibility = False
