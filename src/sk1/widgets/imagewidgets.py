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

import gtk

from sk1 import _
from sk1.resources import images
from sk1.appconst import PROP_RELIEF
from sk1.appconst import EVENT_BUTTON_PRESS, EVENT_CLICKED, EVENT_TOGGLED

class ImageLabel(gtk.EventBox):
	def __init__(self, image_id, tooltip_txt='', cmd=None):
		gtk.EventBox.__init__(self)
		self.label = images.get_image(image_id)
		self.add(self.label)
		if tooltip_txt: self.set_tooltip_text(tooltip_txt)
		if cmd: self.connect(EVENT_BUTTON_PRESS, cmd)

	def set_image(self, image_id):
		self.label.set_from_pixbuf(images.get_pixbuf(image_id))

class ImageButton(gtk.Button):
	def __init__(self, image_id, tooltip_text='', flat=False, cmd=None):
		gtk.Button.__init__(self)
		self.set_image(images.get_image(image_id))
		if flat: self.set_property(PROP_RELIEF, gtk.RELIEF_NONE)
		if tooltip_text: self.set_tooltip_text(tooltip_text)
		if cmd: self.connect(EVENT_CLICKED, cmd)

class ImageStockButton(gtk.Button):
	def __init__(self, image_id, tooltip_text='',
				size=gtk.ICON_SIZE_MENU, flat=False, cmd=None):
		gtk.Button.__init__(self)
		self.set_image(images.get_stock_image(image_id, size))
		if flat: self.set_property(PROP_RELIEF, gtk.RELIEF_NONE)
		if tooltip_text: self.set_tooltip_text(tooltip_text)
		if cmd: self.connect(EVENT_CLICKED, cmd)

class ImageToggleButton(gtk.ToggleButton):
	def __init__(self, image_id, tooltip_text='', cmd=None):
		gtk.ToggleButton.__init__(self)
		self.set_property(PROP_RELIEF, gtk.RELIEF_NONE)
		self.add(images.get_image(image_id))
		if tooltip_text: self.set_tooltip_text(tooltip_text)
		if cmd: self.connect(EVENT_TOGGLED, cmd)

class KeepRatioLabel(ImageLabel):

	value = True

	def __init__(self):
		ImageLabel.__init__(self, images.IMG_KEEP_RATIO, _('Keep aspect ratio'),
						cmd=self.process_click)

	def process_click(self, *args):
		self.value = not self.value
		if self.value:
			self.set_image(images.IMG_KEEP_RATIO)
			self.set_tooltip_text(_('Don\'t keep aspect ratio'))
		else:
			self.set_image(images.IMG_DONT_KEEP_RATIO)
			self.set_tooltip_text(_('Keep aspect ratio'))

