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

from sk1 import const

class Window(Gtk.Window):

	box = None

	def __init__(self):

		Gtk.Window.__init__(self)
		self.box = Gtk.VBox(False, 0)
		self.build()
		self.add(self.box)
		self.show_all()

		self.connect(const.EVENT_DELETE, self.exit)

	def build(self):pass

	def exit(self, *args):pass

	def center(self):
		self.set_position(Gtk.WindowPosition.CENTER)

	def maximize(self):
		self.window.maximize()
