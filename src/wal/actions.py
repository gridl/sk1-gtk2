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

import gtk, gconst

class AppAction(gtk.Action):

	def __init__(self, action_id, label, tooltip, icon, shortcut,
				 callback, channels, validator, args=[]):

		gtk.Action.__init__(self, action_id, label, tooltip, icon)
		self.menuitem = None
		self.tooltip = tooltip
		self.shortcut = shortcut
		self.callback = callback
		self.validator = validator
		self.args = args
		self.icon = icon

		self.connect(gconst.EVENT_ACTIVATE, self.callback)

		self.channels = channels
		self.validator = validator

		if channels:
			connector = channels[0]
			for channel in channels[1:]:
				connector(channel, self.receiver)

	def receiver(self, *args):
		self.set_sensitive(self.validator())

class AppToggleAction(gtk.ToggleAction):

	def __init__(self, action_id, label, tooltip, icon, shortcut,
				 callback, channels, validator, checker, args=[]):

		gtk.ToggleAction.__init__(self, action_id, label, tooltip, icon)
		self.menuitem = None
		self.tooltip = tooltip
		self.shortcut = shortcut
		self.callback = callback
		self.validator = validator
		self.checker = checker
		self.args = args
		self.icon = icon

		self.connect(gconst.EVENT_TOGGLED, self.callback)

		self.channels = channels
		self.validator = validator

		if channels:
			connector = channels[0]
			for channel in channels[1:]:
				connector(channel, self.receiver)

	def receiver(self, *args):
		self.set_sensitive(self.validator())
		self.set_active(self.checker())

class AppModeAction(gtk.RadioAction):

	def __init__(self, action_id, label, tooltip, icon, shortcut,
				 callback, channels, validator, checker, args=[]):

		gtk.RadioAction.__init__(self, action_id, label, tooltip, icon, action_id)
		self.action_id = action_id
		self.menuitem = None
		self.tooltip = tooltip
		self.shortcut = shortcut
		self.callback = callback
		self.validator = validator
		self.checker = checker
		self.args = args
		self.icon = icon

		self.connect(gconst.EVENT_CHANGED, self.do_action)

		self.channels = channels
		self.validator = validator

		if channels:
			connector = channels[0]
			for channel in channels[1:]:
				connector(channel, self.receiver)

	def receiver(self, *args):
		if not self.get_active() and self.checker(self.action_id):
			self.set_active(True)

	def do_action(self, *args):
		if self.get_active() and not self.checker(self.action_id):
			self.callback(self.action_id)
