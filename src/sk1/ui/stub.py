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

from gi.repository import Gtk, Gdk
from sk1.widgets import Canvas

class AppStub(Canvas):

	def __init__(self, mw):
		self.mw = mw
		Canvas.__init__(self)
#		self.nodocs_color = self.mw.get_style().fg[Gtk.StateType.INSENSITIVE]
#		self.modify_bg(Gtk.StateType.NORMAL, self.nodocs_color)
		context = self.mw.get_style_context()
		color = context.get_color(Gtk.StateFlags.INSENSITIVE).to_color()
		print color
#		color = Gdk.Color.from_floats(0.1, 0.1, 0.1)
		self.modify_bg(Gtk.StateType.NORMAL, color)
