# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2014 by Igor E. Novikov
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

import gtk, gconst

from actions import AppAction, AppToggleAction
from boxes import VBox, HBox


class MainWindow(gtk.Window):

	accelgroup = None
	actiongroup = None
	actions = {}

	def __init__(self, action_entries=[], horizontal=False):
		gtk.Window.__init__(self)

		self.create_actions(action_entries)

		self.box = VBox()
		if horizontal: self.box = HBox()
		self.build()
		self.add(self.box)
		self.connect(gconst.EVENT_DELETE, self.event_close)
		self.show_all()

	def build(self):pass

	def event_close(self, *args):return True

	def run(self):gtk.main()
	def exit(self):gtk.main_quit();sys.exit()

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def center(self): self.set_position(gtk.WIN_POS_CENTER)
	def set_title(self, title): gtk.Window.set_title(self, title)
	def set_size(self, w, h): self.set_default_size(w, h)
	def get_size(self): return tuple(gtk.Window.get_size(self))
	def set_min_size(self, w, h): self.set_size_request(w, h)
	def maximize(self): gtk.Window.maximize(self)
	def is_maximized(self):
		return self.window.get_state() == gtk.gdk.WINDOW_STATE_MAXIMIZED

	def create_actions(self, entries):
		if not entries: return
		self.accelgroup = gtk.AccelGroup()
		self.actiongroup = gtk.ActionGroup('MW_Actions')
		self.actions = {}
		for entry in entries:
			if len(entry) == 8:
				action = AppAction(*entry)
			else:
				action = AppToggleAction(*entry)

			self.actions[entry[0]] = action
			if not action.shortcut is None:
				self.actiongroup.add_action_with_accel(action, action.shortcut)
				action.set_accel_group(self.accelgroup)
			else:
				self.actiongroup.add_action(action)
		self.add_accel_group(self.accelgroup)
