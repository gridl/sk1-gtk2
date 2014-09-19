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

class MenuBar(Gtk.MenuBar):

	actions = {}

	def __init__(self):
		Gtk.MenuBar.__init__(self)

	def make_main_menu(self, data):
		menubutton, menu = self.create_menu(data[0])
		self.add_items(menu, data[1])
		self.append(menubutton)

	def create_menu(self, text):
		menu = Gtk.Menu()
		item = Gtk.MenuItem(text)
		item.set_submenu(menu)
		return item, menu

	def add_items(self, parent, items):
		for item in items:
			if item is None:
				parent.append(Gtk.SeparatorMenuItem())
			elif isinstance(item, int):
				action = self.actions[item]
				menuitem = action.create_menu_item()
				action.menuitem = menuitem
				parent.append(menuitem)
			else:
				parent.append(item)
