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

import os, sys
from gi.repository import Gtk

from uc2.application import UCApplication

from sk1 import _, config, events
from sk1.actions import create_actions
from sk1.app_conf import AppData
from sk1.app_cms import AppColorManager
from sk1.inspector import DocumentInspector
from sk1.proxy import AppProxy
from sk1.ui.clipboard import AppClipboard
from sk1.app_palettes import AppPaletteManager
from sk1.ui.mainwindow import MainWindow

class SK1Application(UCApplication):

	appdata = None

	actions = {}
	docs = []
	current_doc = None
	doc_counter = 0

	proxy = None
	inspector = None
	cursors = None

	def __init__(self):

		UCApplication.__init__(self, config.resource_dir)
		self.appdata = AppData()
		config.load(self.appdata.app_config)
		config.resource_dir = os.path.join(self.path, 'share')
		self.default_cms = AppColorManager(self)

		self.inspector = DocumentInspector(self)
		self.proxy = AppProxy(self)
		self.clipboard = AppClipboard(self)
		self.palette_mngr = AppPaletteManager(self)

		self.accelgroup = Gtk.AccelGroup()
		self.actiongroup = Gtk.ActionGroup('BasicAction')

		self.actions = create_actions(self)
		self.mw = MainWindow(self)
		self.proxy.update_references()


	def run(self):
		txt = _('To start create new or open existing document')
		events.emit(events.NO_DOCS)
		events.emit(events.APP_STATUS, txt)
		Gtk.main()

	def exit(self):
		self.mw.hide()
		Gtk.main_quit()
		sys.exit(0)
