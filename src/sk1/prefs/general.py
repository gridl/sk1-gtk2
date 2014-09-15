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

import gtk

from sk1 import _, config, appconst
from sk1.prefs.generic import GenericPrefsPlugin

class GeneralPlugin(GenericPrefsPlugin):

	name = 'GeneralPlugin'
	title = _('General Application Preferences')
	short_title = _('General Preferences')
	icon_stock = gtk.STOCK_PROPERTIES

	def __init__(self, app, dlg, pdxf_config):
		GenericPrefsPlugin.__init__(self, app, dlg, pdxf_config)

	def build(self):
		GenericPrefsPlugin.build(self)
		txt = _('Create new document on start')
		self.newdoc_check = gtk.CheckButton(txt)
		self.newdoc_check.set_active(config.new_doc_on_start)
		self.pack_start(self.newdoc_check, False, True, 5)

	def apply_changes(self):
		config.new_doc_on_start = self.newdoc_check.get_active()

	def restore_defaults(self):
		defaults = config.get_defaults()
		self.newdoc_check.set_active(defaults['new_doc_on_start'])
