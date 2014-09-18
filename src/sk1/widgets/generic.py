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

import gtk, gobject

from uc2.cms import gdk_hexcolor_to_rgb, rgb_to_gdk_hexcolor
from sk1 import const

class CheckButton(gtk.CheckButton):

	def __init__(self, text, state=False, cmd=None):
		gtk.CheckButton.__init__(self, text)
		self.set_active(state)
		if cmd: self.connect(const.EVENT_TOGGLED, cmd)

class SpinButton(gtk.SpinButton):

	def __init__(self, val=0.0, valrange=[0.0, 1.0], step_incr=0.1, cmd=None):
		#value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0
		self.adj = gtk.Adjustment(val, valrange[0], valrange[1], step_incr, 1.0, 0.0)
		gtk.SpinButton.__init__(self, self.adj, 0.1, 2)
		self.set_numeric(True)
		if cmd: self.connect(const.EVENT_VALUE_CHANGED, cmd)

class SpinButtonInt(SpinButton):

	def __init__(self, val=0, valrange=[0, 10], step_incr=1, cmd=None):
		SpinButton.__init__(self, val, valrange, step_incr, cmd)
		self.set_digits(0)

	def get_value(self):
		return self.get_value_as_int()

class ColorButton(gtk.ColorButton):

	def __init__(self, color, title='', cmd=None):
		gtk.ColorButton.__init__(self)
		self.set_color(color)
		if cmd:self.connect(const.EVENT_COLOR_SET, cmd)
		if title:self.set_title(title)

	def set_color(self, color):
		color = gtk.gdk.Color(rgb_to_gdk_hexcolor(color))
		gtk.ColorButton.set_color(self, color)

	def get_color(self):
		color = gtk.ColorButton.get_color(self)
		return tuple(gdk_hexcolor_to_rgb(color.to_string()))

class PangoLabel(gtk.Label):

	def __init__(self, text='', size='', bold=False,
				italic=False, enabled=True, wrap=False):
		gtk.Label.__init__(self)
		markup = '%s'
		if italic:markup = '<i>%s</i>' % (markup)
		if bold:markup = '<b>%s</b>' % (markup)
		if size:markup = '<span size="%s">%s</span>' % (size, markup)
		self.markup = markup
		self.set_markup(markup % (text))
		if not enabled: self.set_sensitive(False)
		if wrap: self.set_line_wrap(True)

	def set_text(self, text):
		self.set_markup(self.markup % (text))

class SimpleListCombo(gtk.ComboBox):

	def __init__(self, listdata=[], cmd=None):
		self.vbox = gtk.VBox(homogeneous=True)
		self.liststore = gtk.ListStore(gobject.TYPE_STRING)
		gtk.ComboBox.__init__(self, self.liststore)
		cell = gtk.CellRendererText()
		self.pack_start(cell, True)
		self.add_attribute(cell, 'text', 0)
		self.set_list(listdata)
		self.vbox.pack_start(self, False, False, 0)
		if cmd: self.connect(const.EVENT_CHANGED, cmd)

	def clear(self):
		self.liststore.clear()

	def set_list(self, datalist=[]):
		if datalist:
			for item in datalist:
				self.append_text(item)
