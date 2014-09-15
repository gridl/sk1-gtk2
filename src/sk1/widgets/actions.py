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

from sk1 import events

class AppAction(gtk.Action):

	def __init__(self, name, label, tooltip, icon, shortcut,
				 callback, channels, validator, args=[]):

		gtk.Action.__init__(self, name, label, tooltip, icon)
		self.menuitem = None
		self.tooltip = tooltip
		self.shortcut = shortcut
		self.callback = callback
		self.events = events
		self.validator = validator
		self.args = args
		self.icon = icon

		self.connect('activate', self.callback)

		self.channels = channels
		self.validator = validator

		if channels:
			for channel in channels:
				events.connect(channel, self.receiver)

	def receiver(self, *args):
		self.set_sensitive(self.validator())

class AppToggleAction(gtk.ToggleAction):

	def __init__(self, name, label, tooltip, icon, shortcut,
				 callback, channels, validator, checker, args=[]):

		gtk.Action.__init__(self, name, label, tooltip, icon)
		self.menuitem = None
		self.tooltip = tooltip
		self.shortcut = shortcut
		self.callback = callback
		self.events = events
		self.validator = validator
		self.checker = checker
		self.args = args
		self.icon = icon

		self.connect('activate', self.callback)

		self.channels = channels
		self.validator = validator

		if channels:
			for channel in channels:
				events.connect(channel, self.receiver)

	def receiver(self, *args):
		self.set_sensitive(self.validator())
		self.set_active(self.checker())