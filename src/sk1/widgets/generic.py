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

class PangoLabel(gtk.Label):

	def __init__(self, text='', size='', bold=False,
				italic=False, enabled=True, wrap=False):
		gtk.Label.__init__(self)
		markup = '%s'
		if italic:markup = '<i>%s</i>' % (markup)
		if bold:markup = '<b>%s</b>' % (markup)
		if size:markup = '<span size="%s">%s</span>' % (size, markup)
		self.set_markup(markup % (text))
		if not enabled: self.set_sensitive(False)
		if wrap: self.set_line_wrap(True)

class SimpleListCombo(gtk.ComboBox):

	def __init__(self, listdata=[]):
		self.vbox = gtk.VBox(homogeneous=True)
		self.liststore = gtk.ListStore(gobject.TYPE_STRING)
		gtk.ComboBox.__init__(self, self.liststore)
		cell = gtk.CellRendererText()
		self.pack_start(cell, True)
		self.add_attribute(cell, 'text', 0)
		self.set_list(listdata)
		self.vbox.pack_start(self, False, False, 0)

	def clear(self):
		self.liststore.clear()

	def set_list(self, list=[]):
		if list:
			for item in list:
				self.append_text(item)
