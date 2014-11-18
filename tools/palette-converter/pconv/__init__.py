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

from pconv.app_conf import AppConfig, AppData

global config

def dummy_translator(text):
	return text

_ = dummy_translator
config = None

def pconv_run():

	global config

	config = AppConfig(__path__[0])
	appdata = AppData()
	config.load(appdata.app_config)

	if config.mw_disable_global_menu:
		os.environ["UBUNTU_MENUPROXY"] = "0"
	if config.mw_disable_overlay_scroll:
		os.environ["LIBOVERLAY_SCROLLBAR"] = "0"

	from pconv.pcapp import Application

	app = Application(appdata)
	app.run()
