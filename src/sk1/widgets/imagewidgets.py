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

import os, gtk

from sk1 import _, config
from sk1.resources import images

class ImageLabel(gtk.EventBox):

	def __init__(self, image_id, tooltip_txt=''):
		gtk.EventBox.__init__(self)
		self.label = images.get_image(image_id)
		self.add(self.label)
		if tooltip_txt: self.set_tooltip_text(tooltip_txt)

class ImageButton(gtk.Button):
	def __init__(self, text, path):
		gtk.Button.__init__(self)
		self.set_property('relief', gtk.RELIEF_NONE)
		loader = gtk.gdk.pixbuf_new_from_file
		image = gtk.Image()
		pixbuf = loader(os.path.join(config.resource_dir, *path))
		image.set_from_pixbuf(pixbuf)
		self.add(image)
		if text:
			self.set_tooltip_text(text)

class ImageStockButton(gtk.Button):
	def __init__(self, text='', stock=gtk.STOCK_HELP, flat=True):
		gtk.Button.__init__(self)
		if flat: self.set_property('relief', gtk.RELIEF_NONE)
		image = gtk.Image()
		image.set_from_stock(stock, gtk.ICON_SIZE_MENU)
		self.set_image(image)
		if text: self.set_tooltip_text(text)

class ImageToggleButton(gtk.ToggleButton):
	def __init__(self, text, path):
		gtk.ToggleButton.__init__(self)
		self.set_property('relief', gtk.RELIEF_NONE)
		loader = gtk.gdk.pixbuf_new_from_file
		image = gtk.Image()
		pixbuf = loader(os.path.join(config.resource_dir, *path))
		image.set_from_pixbuf(pixbuf)
		self.add(image)
		if text:
			self.set_tooltip_text(text)

class KeepRatioLabel(gtk.EventBox):

	value = True

	def __init__(self):
		path_true = 'object-keep-ratio.png'
		path_false = 'object-dont-keep-ratio.png'

		loader = gtk.gdk.pixbuf_new_from_file
		self.image_true = loader(os.path.join(config.resource_dir, 'icons', path_true))

		loader = gtk.gdk.pixbuf_new_from_file
		self.image_false = loader(os.path.join(config.resource_dir, 'icons', path_false))

		gtk.EventBox.__init__(self)
		self.image = gtk.Image()
		self.image.set_from_pixbuf(self.image_true)
		self.add(self.image)
		self.connect('button-press-event', self.process_click)
		self.set_tooltip_text(_('Keep aspect ratio'))

	def process_click(self, *args):
		if self.value:
			self.value = False
			self.image.set_from_pixbuf(self.image_false)
			self.set_tooltip_text(_('Don\'t keep aspect ratio'))
		else:
			self.value = True
			self.image.set_from_pixbuf(self.image_true)
			self.set_tooltip_text(_('Keep aspect ratio'))
