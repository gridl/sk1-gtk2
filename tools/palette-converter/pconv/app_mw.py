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


import wal

from pconv import config

class AppMainWindow(wal.MainWindow):

	app = None

	def __init__(self, app, action_entries=[]):
		self.app = app
		wal.MainWindow.__init__(self, action_entries)

	def build(self):
		self.set_min_size(*config.mw_min_size)
		self.set_size(*config.mw_size)
		self.center()
		self.set_title(self.app.appdata.app_name)
