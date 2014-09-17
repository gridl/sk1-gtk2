# -*- coding: utf-8 -*-
#
#	Copyright (C) 2012-2014 by Igor E. Novikov
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

from sk1 import _, config, const, rc

from sk1.prefs.generic import GenericPrefsPlugin

class TestPlugin(GenericPrefsPlugin):

	name = 'TestPlugin'
	title = _('Test Preference Plugin')
	short_title = _('Test Plugin')
	image_id = rc.IMG_CTX_PORTRAIT
	cid = const.PREFS_DOC_PLUGIN

	def __init__(self, app, dlg, fmt_config):
		GenericPrefsPlugin.__init__(self, app, dlg, fmt_config)

	def build(self):
		GenericPrefsPlugin.build(self)

	def apply_changes(self):pass

	def restore_defaults(self):pass


class Test2Plugin(GenericPrefsPlugin):

	name = 'Test3Plugin'
	title = _('Test3 Preference Plugin')
	short_title = _('Test3 Plugin')
	cid = const.PREFS_DOC_PLUGIN

	def __init__(self, app, dlg, fmt_config):
		GenericPrefsPlugin.__init__(self, app, dlg, fmt_config)
