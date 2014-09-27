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


import wal

from sk1 import events
from sk1.parts import PagerWidget, ColorMonitorWidget

class AppStatusbar(wal.HBox):

	plugins_dict = {}
	plugins = []

	def __init__(self, app, master):
		self.app = app
		wal.HBox.__init__(self, master)

		self.pager = PagerWidget(self.app, self)
		self.pack(self.pager, padding=5)

		self.msg_label = wal.DecorLabel(self, size=-1)
		self.pack(self.msg_label)

		self.cmw = ColorMonitorWidget(self.app)
		self.pack(self.cmw, end=True)

		events.connect(events.APP_STATUS, self.show_message)

	def show_message(self, args):
		self.msg_label.set_text(args[0])
