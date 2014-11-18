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

from pconv import _, config, actions

class AppMainWindow(wal.MainWindow):

	app = None

	def __init__(self, app, action_entries=[]):
		self.app = app
		wal.MainWindow.__init__(self, action_entries)

	def build(self):
		self.app.actions = self.actions
		self.app.mw = self

		self.mb = AppMenubar(self)
		self.toolbar = AppToolbar(self)

		#---CENTRAL PART
		self.workarea = wal.HidableVArea(self)

		#---SPLASH
		self.nb_splash = Splash(self.workarea)
		self.workarea.pack2(self.nb_splash, True, True)

		#---CENTRAL PART END

		self.pack(self.workarea, True, True)

		self.set_min_size(*config.mw_min_size)
		self.set_size(*config.mw_size)
		self.center()
		self.set_title(self.app.appdata.app_name)

class AppMenubar(wal.MW_Menu):

	def __init__(self, mw):
		wal.MW_Menu.__init__(self, mw)

	def build(self):

		#----FILE MENU
		self.file_item, self.file_menu = self.create_menu(_("_File"))
		items = [actions.NEW,
				 None,
				 actions.OPEN,
		]
		self.add_items(self.file_menu, items)

		self.append(self.file_item)

class AppToolbar(wal.MW_Toolbar):

	def __init__(self, mw):
		wal.MW_Toolbar.__init__(self, mw)

	def build(self):
		entries = [
				actions.NEW, None, actions.OPEN,
			   ]
		self.add_toolbar_items(entries)

class Splash(wal.ImgPlate):

	def __init__(self, master):
		wal.ImgPlate.__init__(self, master, bg=wal.DARK_GRAY)
#		self.cairo_img = self.load_image(rc.IMG_CAIRO_BANNER)
#		self.triada_img = self.load_image(rc.IMG_SPLASH_TRIADA)

	def repaint(self):pass
#		if config.show_cairo_splash:
#			w, h = self.get_size()
#
#			x = 5
#			y = h - self.get_image_size(self.cairo_img)[1] - 5
#			self.draw_image(self.cairo_img, x, y)
#
#			x = w - self.get_image_size(self.triada_img)[0] + 80
#			y = h - self.get_image_size(self.triada_img)[1] + 80
#			self.draw_image(self.triada_img, x, y)
