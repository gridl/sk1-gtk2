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

	def __init__(self, master):
		self.master = master
		gtk.VBox.__init__(self)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		if end: self.pack_end(child, expand, fill, padding)
		else: self.pack_start(child, expand, fill, padding)

	def remove(self, child):
		gtk.VBox.remove(self, child)


class HBox(gtk.HBox):

	def __init__(self, master):
		self.master = master
		gtk.HBox.__init__(self)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		if end: self.pack_end(child, expand, fill, padding)
		else: self.pack_start(child, expand, fill, padding)

	def remove(self, child):
		gtk.HBox.remove(self, child)

class HidableVBox(VBox):

	visibility = True

	def __init__(self, master):
		VBox.__init__(self, master)

		self.box = VBox(self)
		VBox.pack(self, self.box, True, True)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def remove(self, child):
		self.box.remove(child)

	def set_visible(self, visible):
		if visible and not self.visibility:
			VBox.pack(self, self.box, True, True)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			VBox.remove(self, self.box)
			self.visibility = False
			self.show_all()

class HidableHBox(HBox):

	visibility = True

	def __init__(self, master):
		HBox.__init__(self, master)

		self.box = HBox(self)
		HBox.pack(self, self.box, True, True)

	def pack(self, child, expand=False, fill=False, padding=0, end=False):
		self.box.pack(child, expand, fill, padding, end)

	def remove(self, child):
		self.box.remove(child)

	def set_visible(self, visible):
		if visible and not self.visibility:
			HBox.pack(self, self.box, True, True)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			HBox.remove(self, self.box)
			self.visibility = False
			self.show_all()

class HidableVArea(VBox):

	visibility = False

	def __init__(self, master):
		VBox.__init__(self, master)

		self.box = VBox(self)
		self.box2 = VBox(self)
		VBox.pack(self, self.box2, True, True)

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
			VBox.pack(self, self.box, True, True)
			self.visibility = True
			self.show_all()
		elif not visible and self.visibility:
			VBox.remove(self, self.box)
			VBox.pack(self, self.box2, True, True)
			self.visibility = False
			self.show_all()





