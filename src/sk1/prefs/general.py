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

from sk1 import _, config
from sk1.prefs.generic import GenericPrefsPlugin

class GeneralPlugin(GenericPrefsPlugin):

	name = 'GeneralPlugin'
	title = _('General Application Preferences')
	short_title = _('General')
	icon_stock = wal.STOCK_PROPERTIES

	def __init__(self, app, dlg, fmt_config):
		GenericPrefsPlugin.__init__(self, app, dlg, fmt_config)

	def build(self):
		GenericPrefsPlugin.build(self)

		txt = _('Create new document on start')
		self.newdoc_check = wal.CheckButton(self, txt, config.new_doc_on_start)
		self.pack_start(self.newdoc_check, False, True, 5)

		txt = _('Store application window size')
		self.winsize_check = wal.CheckButton(self, txt, config.mw_store_size)
		self.pack_start(self.winsize_check, False, True, 5)

		txt = _('Maximize application window on start')
		self.maxwin_check = wal.CheckButton(self, txt, config.mw_keep_maximized)
		self.pack_start(self.maxwin_check, False, True, 5)

	def apply_changes(self):
		config.new_doc_on_start = self.newdoc_check.get_active()
		config.mw_store_size = self.winsize_check.get_active()
		config.mw_keep_maximized = self.maxwin_check.get_active()

	def restore_defaults(self):
		defaults = config.get_defaults()
		self.newdoc_check.set_active(defaults['new_doc_on_start'])
		self.winsize_check.set_active(defaults['mw_store_size'])
		self.maxwin_check.set_active(defaults['mw_keep_maximized'])
