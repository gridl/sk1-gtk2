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


import gtk

from sk1 import events
from sk1.widgets import ColorMonitorWidget
from sk1.widgets import PagerWidget

class AppStatusbar(gtk.HBox):

	plugins_dict = {}
	plugins = []

	def __init__(self, mw):
		gtk.HBox.__init__(self)

		self.mw = mw
		self.app = mw.app

		self.pager = PagerWidget(self.app)
		self.pack_start(self.pager, False, False, 5)

		self.msg_label = gtk.Label()
		self.pack_start(self.msg_label, False, False, 0)

		self.cmw = ColorMonitorWidget(self.app)
		self.pack_end(self.cmw, False, False, 0)

		vbox = gtk.VBox()
		spacer = gtk.EventBox()
		vbox.pack_start(spacer, False, False, 10)
		self.pack_end(vbox, False, False, 0)

		events.connect(events.APP_STATUS, self.show_message)

	def show_message(self, args):
		self.msg_label.set_text(args[0])
