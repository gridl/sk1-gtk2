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

import sys

import gtk, gconst, rc

from actions import AppAction, AppToggleAction, AppRadioAction
from boxes import VBox, HBox


class MainWindow(gtk.Window):

	accelgroup = None
	actiongroup = None
	actions = {}

	def __init__(self, action_entries=[], horizontal=False):
		gtk.Window.__init__(self)

		self.create_actions(action_entries)

		self.box = VBox(self)
		if horizontal: self.box = HBox(self)
		self.build()
		self.add(self.box)
		self.connect(gconst.EVENT_DELETE, self.event_close)

	def build(self):pass

	def event_close(self, *args):
		self.exit()
		return False

	def run(self):
		self.show_all()
		gtk.main()

	def exit(self):gtk.main_quit();sys.exit()

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def pack_all(self, childs, expand=False, fill=False, padding=0, end=False):
		self.box.pack_all(childs, expand, fill, padding, end)

	def center(self): self.set_position(gtk.WIN_POS_CENTER)
	def set_title(self, title): gtk.Window.set_title(self, title)
	def set_size(self, w, h): gtk.Window.set_default_size(self, w, h)
	def get_size(self): return tuple(gtk.Window.get_size(self))
	def set_min_size(self, w, h): self.set_size_request(w, h)
	def maximize(self): gtk.Window.maximize(self)
	def is_maximized(self):
		return self.window.get_state() == gtk.gdk.WINDOW_STATE_MAXIMIZED

	def create_actions(self, entries):
		if not entries: return
		self.accelgroup = gtk.AccelGroup()
		self.actiongroup = gtk.ActionGroup('MW_Actions')
		self.modegroup = None
		self.actions = {}
		for entry in entries:
			action_id = entry[0]
			if action_id < 100:
				action = AppRadioAction(*entry)
			elif action_id < 1000:
				action = AppAction(*entry)
			else:
				action = AppToggleAction(*entry)

			self.actions[entry[0]] = action
			if action_id < 100:
				if self.modegroup is None:
					self.modegroup = action
				else:
					action.set_group(self.modegroup)
			if not action.shortcut is None:
				self.actiongroup.add_action_with_accel(action, action.shortcut)
				action.set_accel_group(self.accelgroup)
			else:
				self.actiongroup.add_action(action)
		self.add_accel_group(self.accelgroup)


class MW_Toolbar(gtk.Toolbar):

	def __init__(self, master):
		self.master = master
		self.actions = master.actions
		gtk.Toolbar.__init__(self)
		self.set_style(gtk.TOOLBAR_ICONS)
		self.build()
		master.pack(self)

	def build(self):pass

	def add_toolbar_items(self, entries):
		index = 0
		for entry in entries:
			if entry is None:
				button = gtk.SeparatorToolItem()
			else:
				action = self.actions[entry]
				button = action.create_tool_item()
			self.insert(button, index)
			index += 1


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
				if action.is_toggle() or not action.icon:
					menuitem = action.create_menu_item()
				else:
					menuitem = gtk.ImageMenuItem()
					menuitem.set_label(action.get_label())
					menuitem.set_image(rc.get_image(action.icon, rc.FIXED16))
					menuitem.set_accel_path(action.get_accel_path())
					action.connect_proxy(menuitem)
				action.menuitem = menuitem
				parent.append(menuitem)
			else:
				parent.append(item)
