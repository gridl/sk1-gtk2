# -*- coding: utf-8 -*-
#
#	Copyright (C) 2013 by Igor E. Novikov
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

import gtk, os

from sk1 import _, config, events, appconst
from sk1.widgets.hidable import HidableHBox
from sk1.widgets.generic import PangoLabel

class PagerWidget(HidableHBox):

	start = None
	left = None
	label = None
	right = None
	end = None

	def __init__(self, app):

		HidableHBox.__init__(self)
		self.app = app
		self.insp = app.inspector

		self.hbox = gtk.HBox()
		self.box.pack_start(self.hbox, False, False, 0)

		self.start = PagerButton('pager-arrow-start.png')
		self.hbox.pack_start(self.start, False, False, 0)
		self.start.connect('clicked', self.goto_start)

		self.left = PagerButton('pager-arrow-left.png')
		self.hbox.pack_start(self.left, False, False, 0)
		self.left.connect('clicked', self.goto_left)

		self.label = PangoLabel(size=appconst.TXT_SMALLER)
		self.hbox.pack_start(self.label, False, False, 5)

		self.right = PagerButton('pager-arrow-right.png')
		self.hbox.pack_start(self.right, False, False, 0)
		self.right.connect('clicked', self.goto_right)

		self.end = PagerButton('pager-arrow-end.png')
		self.hbox.pack_start(self.end, False, False, 0)
		self.end.connect('clicked', self.goto_end)

		self.hbox.pack_start(gtk.VSeparator(), False, False, 0)

		self.update_pager()
		events.connect(events.DOC_CHANGED, self.update_pager)
		events.connect(events.DOC_MODIFIED, self.update_pager)
		events.connect(events.DOC_CLOSED, self.update_pager)
		events.connect(events.NO_DOCS, self.update_pager)

		self.show_all()

	def update_pager(self, *args):
		if not self.insp.is_doc():
			self.set_visible(False)
			return
		self.set_visible(True)

		presenter = self.app.current_doc

		pages = presenter.get_pages()
		current_index = pages.index(presenter.active_page)

		text = _("Page %i of %i") % (current_index + 1, len(pages))
		self.label.set_text(text)

		if current_index:
			self.start.set_sensitive(True)
			self.left.set_sensitive(True)
		else:
			self.start.set_sensitive(False)
			self.left.set_sensitive(False)

		if current_index == len(pages) - 1:
			self.end.set_sensitive(False)
		else:
			self.end.set_sensitive(True)
		self.show_all()

	def goto_start(self, *args):
		self.app.current_doc.goto_page(0)

	def goto_left(self, *args):
		pages = self.app.current_doc.get_pages()
		current_index = pages.index(self.app.current_doc.active_page)
		self.app.current_doc.goto_page(current_index - 1)

	def goto_right(self, *args):
		pages = self.app.current_doc.get_pages()
		current_index = pages.index(self.app.current_doc.active_page)
		if current_index < len(pages) - 1:
			self.app.current_doc.goto_page(current_index + 1)
		else:
			self.app.current_doc.app.proxy.insert_page()

	def goto_end(self, *args):
		pages = self.app.current_doc.get_pages()
		self.app.current_doc.goto_page(len(pages) - 1)

class PagerButton(gtk.Button):
	def __init__(self, file_name):
		gtk.Button.__init__(self)
		self.set_property('relief', gtk.RELIEF_NONE)
		image_dir = os.path.join(config.resource_dir, 'icons', 'pager')
		loader = gtk.gdk.pixbuf_new_from_file
		image = gtk.Image()
		pixbuf = loader(os.path.join(image_dir, file_name))
		image.set_from_pixbuf(pixbuf)
		self.add(image)


