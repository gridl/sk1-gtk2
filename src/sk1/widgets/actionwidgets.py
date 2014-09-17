# -*- coding: utf-8 -*-
#
#	Copyright (C) 2013-2014 by Igor E. Novikov
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

from sk1.resources import icons
from sk1.appconst import PROP_RELIEF

class ActionButton(gtk.Button):
	def __init__(self, action):
		gtk.Button.__init__(self)
		if action.icon:
			icon = gtk.image_new_from_stock(action.icon, icons.FIXED16)
			self.add(icon)
		self.set_property(PROP_RELIEF, gtk.RELIEF_NONE)
		self.set_tooltip_text(action.tooltip)
		action.connect_proxy(self)

class ActionToggleButton(gtk.ToggleButton):
	def __init__(self, action):
		gtk.ToggleButton.__init__(self)
		if action.icon:
			icon = gtk.image_new_from_stock(action.icon, icons.FIXED16)
			self.add(icon)
		self.set_property(PROP_RELIEF, gtk.RELIEF_NONE)
		self.set_tooltip_text(action.tooltip)
		action.connect_proxy(self)