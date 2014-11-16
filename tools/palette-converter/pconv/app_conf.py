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

import os

from uc2.uc_conf import UCConfig, UCData
from uc2.utils.fs import expanduser_unicode

from pconv import events

class AppData(UCData):

	app_name = 'sK1 Palette Converter'
	app_proc = 'pconv'
	app_org = 'sK1 Project'
	app_domain = 'sk1project.org'
	app_icon = None
	doc_icon = None
	version = "1.0"
	app_config_dir = expanduser_unicode(os.path.join('~', '.config', 'pconv'))

	def __init__(self):

		UCData.__init__(self)

class AppConfig(UCConfig):

	def __init__(self, path):
		UCConfig.__init__(self)

	def __setattr__(self, attr, value):
		if attr == 'filename': return
		if not hasattr(self, attr) or getattr(self, attr) != value:
			self.__dict__[attr] = value
			events.emit(events.CONFIG_MODIFIED, attr, value)

	def get_defaults(self):
		defaults = AppConfig.__dict__
		defaults.update(UCConfig.get_defaults(self))
		return defaults

	#============== GENERIC SECTION ===================

	mw_size = (700, 500)
	mw_min_size = (700, 500)
