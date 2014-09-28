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

import wal

class GenericPlugin(wal.HBox):

	name = 'GenericPlugin'

	def __init__(self, app, master):
		wal.HBox.__init__(self, master)
		self.app = app
		self.actions = self.app.actions
		self.insp = self.app.inspector
		self.pack(wal.VLine(self), padding=2, end=True)
		self.build()

	def build(self):pass
