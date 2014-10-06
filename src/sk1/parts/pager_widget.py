# -*- coding: utf-8 -*-
#
#	Copyright (C) 2013-2014 by Igor E. Novikov
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

from sk1 import _, events, rc

class PagerWidget(wal.HBox):

	start = None
	left = None
	label = None
	right = None
	end = None

	def __init__(self, app, master):

		wal.HBox.__init__(self, master)
		self.app = app
		self.insp = app.inspector

		self.start = wal.ImgButton(self, rc.IMG_PAGER_START,
								cmd=self.first_page, flat=True)
		self.pack(self.start)

		self.left = wal.ImgButton(self, rc.IMG_PAGER_PREV,
								cmd=self.prev_page, flat=True)
		self.pack(self.left)

		self.label = wal.DecorLabel(self)
		self.pack(self.label, False, False, 5)

		self.right = wal.ImgButton(self, rc.IMG_PAGER_NEXT,
								cmd=self.next_page, flat=True)
		self.pack(self.right)

		self.end = wal.ImgButton(self, rc.IMG_PAGER_END,
								cmd=self.last_page, flat=True)
		self.pack(self.end)

		self.pack(wal.VLine(self))

		self.update_pager()
		events.connect(events.DOC_CHANGED, self.update_pager)
		events.connect(events.DOC_MODIFIED, self.update_pager)

	def update_pager(self, *args):
		if not self.insp.is_doc():return

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

	def first_page(self, *args):
		self.app.current_doc.goto_page(0)

	def prev_page(self, *args):
		pages = self.app.current_doc.get_pages()
		current_index = pages.index(self.app.current_doc.active_page)
		self.app.current_doc.goto_page(current_index - 1)

	def next_page(self, *args):
		pages = self.app.current_doc.get_pages()
		current_index = pages.index(self.app.current_doc.active_page)
		if current_index < len(pages) - 1:
			self.app.current_doc.goto_page(current_index + 1)
		else:
			self.app.current_doc.app.proxy.insert_page()

	def last_page(self, *args):
		pages = self.app.current_doc.get_pages()
		self.app.current_doc.goto_page(len(pages) - 1)



