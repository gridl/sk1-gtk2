# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2014 by Igor E. Novikov
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

import gtk, wal

from sk1 import config, events, rc
from sk1.ui.menubar import AppMenubar
from sk1.ui.toolbar import AppToolbar
from sk1.ui.tools import AppTools
from sk1.ui.palette import HPalette
from sk1.ui.statusbar import AppStatusbar
from sk1.context import ContextPanel
from sk1.plugins import PluginPanel

class AppMainWindow(wal.MainWindow):

	canvas = None
	doc_index = 1

	def __init__(self, app, action_entries):
		self.app = app
		wal.MainWindow.__init__(self, action_entries)

	def build(self):
		self.app.actions = self.actions
		self.app.mw = self

		self.mb = AppMenubar(self)
		self.toolbar = AppToolbar(self)

		#---CENTRAL PART
		self.workarea = wal.HidableVArea(self)

		self.workarea.pack(wal.HLine(self.workarea))
		self.workarea.pack(ContextPanel(self.app, self.workarea))
		self.workarea.pack(wal.HLine(self.workarea))

		hbox = wal.HBox(self.workarea)
		self.tools = AppTools(self.app, hbox)
		hbox.pack_start(self.tools, False, False, 1)
		self.inner_hpaned = gtk.HPaned()
		self.nb = gtk.Notebook()
		self.nb.connect('switch-page', self.change_doc)
		self.nb.set_property('scrollable', True)
		self.inner_hpaned.pack1(self.nb, 1, 0)

		self.plugin_panel = PluginPanel(self)

		hbox.pack_start(self.inner_hpaned, True, True, 1)
		self.workarea.pack(hbox, True, True)

		#---SPLASH
		self.nb_splash = Splash(self.workarea)
		self.workarea.pack2(self.nb_splash, True, True)

		self.hpalette = HPalette(self.app, self.workarea)
		self.workarea.pack(self.hpalette, padding=2)

		self.workarea.pack(wal.HLine(self.workarea))

		self.statusbar = AppStatusbar(self.app, self.workarea)
		self.workarea.pack(self.statusbar)

		#---CENTRAL PART END

		self.pack(self.workarea, True, True)

		self.set_win_title()
		self.set_min_size(*config.mw_min_size)
		if config.mw_store_size: self.set_size(*config.mw_size)

		self.set_icon_from_file(rc.get_image_path(rc.IMG_APP_ICON))
		self.center()

		if config.mw_maximized: self.maximize()

	def event_close(self, *args):
		if self.app.exit_request(): self.exit()
		return False

	def set_win_title(self, docname=''):
		if docname:
			title = '[%s] - %s' % (docname, self.app.appdata.app_name)
			self.set_title(title)
		else:
			self.set_title(self.app.appdata.app_name)

	def add_tab(self, da):
		if not self.nb.get_n_pages():
			self.workarea.set_visible(True)
		index = self.nb.append_page(da, da.tab_caption)
		da.show_all()
		self.nb.show_all()
		self.nb.set_current_page(index)
		self.set_win_title(da.presenter.doc_name)

	def remove_tab(self, tab):
		self.nb.remove_page(self.nb.page_num(tab))
		if not self.nb.get_n_pages():
			self.set_win_title()
			self.app.current_doc = None
			self.workarea.set_visible(False)

	def change_doc(self, *args):
		da = self.nb.get_nth_page(args[2])
		self.app.current_doc = da.presenter
		self.set_win_title(da.caption)
		events.emit(events.DOC_CHANGED, self)

	def set_tab_title(self, tab, title):
		tab.set_caption(title)
		if self.nb.page_num(tab) == self.nb.get_current_page():
			self.set_win_title(title)

	def set_active_tab(self, tab):
		self.nb.set_current_page(self.nb.page_num(tab))

class Splash(wal.ImgPlate):

	def __init__(self, master):
		wal.ImgPlate.__init__(self, master, bg=wal.DARK_GRAY)
		self.cairo_img = self.load_image(wal.IMG_CAIRO_BANNER)
		self.triada_img = self.load_image(wal.IMG_SPLASH_TRIADA)

	def repaint(self):
		if config.show_cairo_splash:
			w, h = self.get_size()

			x = 5
			y = h - self.cairo_img.get_height() - 5
			self.draw_image(self.cairo_img, x, y)

			x = w - self.triada_img.get_width() + 80
			y = h - self.triada_img.get_height() + 80
			self.draw_image(self.triada_img, x, y)



