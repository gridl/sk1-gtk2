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

import gtk, rc

class ColorPlate(gtk.DrawingArea):

	def __init__(self, master, size=(), bgcolor=()):
		self.master = master
		gtk.DrawingArea.__init__()
		if size: self.set_size(*size)
		if bgcolor: self.set_bgcolor(bgcolor)

	def set_size(self, w, h): self.set_size_request(w, h)
	def get_size(self): return tuple(self.allocation)[2:]
	def set_bgcolor(self, color):
		self.modify_bg(gtk.STATE_NORMAL, rc.rgb_to_gdkcolor(color))
	def get_bgcolor(self):
		return rc.gdkcolor_to_rgb(self.get_style().bg[gtk.STATE_NORMAL])
