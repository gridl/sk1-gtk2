# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2012 by Igor E. Novikov
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

from sk1 import events, rc

class AppDocBook(wal.NoteBook):

	docs = []

	def __init__(self, master, app):
		self.app = app
		wal.NoteBook.__init__(self, master)
		self.set_property('scrollable', True)
		events.connect(events.DOC_CHANGED, self.doc_changed)
		events.connect(events.DOC_MODIFIED, self.doc_modified)
		events.connect(events.DOC_SAVED, self.doc_saved)

	def change_doc(self, *args):pass

	def doc_changed(self, *args):pass

	def doc_modified(self, *args):pass

	def doc_saved(self, *args):pass



