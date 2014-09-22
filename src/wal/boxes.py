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

class VBox(gtk.VBox):

	def __init__(self):
		gtk.VBox.__init__(self)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		if end: self.pack_end(child, expand, fill, padding)
		else: self.pack_start(child, expand, fill, padding)


class HBox(gtk.HBox):

	def __init__(self):
		gtk.HBox.__init__(self)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		if end: self.pack_end(child, expand, fill, padding)
		else: self.pack_start(child, expand, fill, padding)

class HidableVBox(VBox):

	visibility = False

	def __init__(self):
		VBox.__init__(self)

		self.box = VBox()

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def remove(self, child):
		self.box.remove(child)

	def set_visible(self, visible):
		if visible and not self.visibility:
			VBox.pack(self, self.box)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			VBox.remove(self, self.box)
			self.visibility = False
			self.show_all()

class HidableHBox(HBox):

	visibility = False

	def __init__(self):
		HBox.__init__(self)

		self.box = HBox()

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def remove(self, child):
		self.box.remove(child)

	def set_visible(self, visible):
		if visible and not self.visibility:
			HBox.pack(self, self.box)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			HBox.remove(self, self.box)
			self.visibility = False
			self.show_all()

class HidableVArea(VBox):

	visibility = False

	def __init__(self):
		VBox.__init__(self)

		self.box = VBox()
		self.box2 = VBox()
		self.pack(self.box2)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def remove(self, child):
		self.box.remove(child)

	def pack2(self, child, expand=False, fill=False, padding=0, end=False):
		self.box2.pack(child, expand, fill, padding, end)

	def remove2(self, child):
		self.box2.remove(child)

	def set_visible(self, visible):
		if visible and not self.visibility:
			VBox.remove(self, self.box2)
			VBox.pack(self.box)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			VBox.remove(self, self.box)
			VBox.pack(self.box2)
			self.visibility = False
			self.show_all()





