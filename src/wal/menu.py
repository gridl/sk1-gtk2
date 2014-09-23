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

import gtk

class MW_Menu(gtk.MenuBar):

	def __init__(self, master):
		self.master = master
		self.actions = master.actions
		gtk.MenuBar.__init__(self)
		self.build()
		master.pack(self)

	def build(self):pass

	def create_menu(self, text):
		menu = gtk.Menu()
		item = gtk.MenuItem(text)
		item.set_submenu(menu)
		return item, menu

	def add_items(self, parent, items):
		for item in items:
			if item is None:
				parent.append(gtk.SeparatorMenuItem())
			elif isinstance(item, int):
				action = self.actions[item]
				menuitem = action.create_menu_item()
				action.menuitem = menuitem
				parent.append(menuitem)
			else:
				parent.append(item)
