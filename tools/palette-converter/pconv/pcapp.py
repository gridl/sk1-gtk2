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


from uc2.application import UCApplication

from pconv.inspector import DocumentInspector
from pconv.proxy import AppProxy
from pconv.app_mw import AppMainWindow

class Application(UCApplication):

	docs = []

	def __init__(self, appdata):

		UCApplication.__init__(self)
		self.appdata = appdata

		self.insp = DocumentInspector(self)
		self.proxy = AppProxy(self)

		self.mw = AppMainWindow(self)
		self.proxy.update_references()

	def run(self):
		self.mw.run()