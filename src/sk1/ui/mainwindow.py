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

from sk1 import config
from sk1.widgets import Window, HLine
from sk1.ui.menubar import AppMenuBar
from sk1.ui.toolbar import AppToolBar
from sk1.ui.ctxtoolbar import CtxToolBar

class MainWindow(Window):

	def __init__(self, app):
		self.app = app
		Window.__init__(self)

	def build(self):
		self.mb = AppMenuBar(self)
		self.box.pack_start(self.mb, False, False, 0)

		self.tb = AppToolBar(self)
		self.box.pack_start(self.tb, False, False, 0)

		if config.primary_toolbar_style:
			self.tb.set_primary_toolbar_style()
		else:
			self.box.pack_start(HLine(), False, False, 0)

		self.ctx = CtxToolBar(self)
		self.box.pack_start(self.ctx, False, False, 0)
		self.box.pack_start(HLine(), False, False, 0)

		self.set_win_title()
		self.set_size_request(config.mw_min_width, config.mw_min_height)
		self.center()
		if config.mw_maximized: self.maximize()

	def exit(self, *args):
		if self.app.exit():
			return False
		else:
			return True

	def set_win_title(self, docname=''):
		if docname:
			title = '[%s] - %s' % (docname, self.app.appdata.app_name)
			self.set_title(title)
		else:
			self.set_title(self.app.appdata.app_name)
