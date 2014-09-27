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

import os, wal
import gtk

from sk1 import _, config
from sk1.parts import HPaletteWidget

class HPalette(wal.HidableHBox):

	def __init__(self, mw):
		wal.HidableHBox.__init__(self, mw)
		self.mw = mw
		self.app = mw.app

		self.pack(wal.FImgButton(self, wal.IMG_PALETTE_DOUBLE_ARROW_LEFT,
								cmd=self.action_dback, repeat=True))

		self.pack(wal.FImgButton(self, wal.IMG_PALETTE_ARROW_LEFT,
								cmd=self.action_back, repeat=True))

		self.no_color = NoColorButton(self)
		self.pack(self.no_color)

		self.palwidget = HPaletteWidget(self.app)
		self.pack(self.palwidget, True, True, 1)

		self.pack(wal.FImgButton(self, wal.IMG_PALETTE_ARROW_RIGHT,
								cmd=self.action_forward, repeat=True))

		self.pack(wal.FImgButton(self, wal.IMG_PALETTE_DOUBLE_ARROW_RIGHT,
								cmd=self.action_dforward, repeat=True))


	def action_dforward(self, *args):
		self.palwidget.position -= 20
		if self.palwidget.position < -self.palwidget.max_pos:
			self.palwidget.position = -self.palwidget.max_pos
		self.palwidget.queue_draw()

	def action_forward(self, *args):
		self.palwidget.position -= 1
		if self.palwidget.position < -self.palwidget.max_pos:
			self.palwidget.position = -self.palwidget.max_pos
		self.palwidget.queue_draw()

	def action_back(self, *args):
		self.palwidget.position += 1
		if self.palwidget.position > 0:
			self.palwidget.position = 0
		self.palwidget.queue_draw()

	def action_dback(self, *args):
		self.palwidget.position += 20
		if self.palwidget.position > 0:
			self.palwidget.position = 0
		self.palwidget.queue_draw()



class PalButton(gtk.Button):
	def __init__(self, file_name):
		gtk.Button.__init__(self)
		self.set_property('relief', gtk.RELIEF_NONE)
		image_dir = os.path.join(config.resource_dir, 'icons', 'palette')
		loader = gtk.gdk.pixbuf_new_from_file
		image = gtk.Image()
		pixbuf = loader(os.path.join(image_dir, file_name))
		image.set_from_pixbuf(pixbuf)
		self.add(image)

class NoColorButton(gtk.EventBox):

	def __init__(self, master):
		gtk.EventBox.__init__(self)
		self.app = master.app
		self.set_size_request(-1, 22)
		image_dir = os.path.join(config.resource_dir, 'icons', 'palette')
		loader = gtk.gdk.pixbuf_new_from_file
		image = gtk.Image()
		pixbuf = loader(os.path.join(image_dir, 'no-color.png'))
		image.set_from_pixbuf(pixbuf)
		self.add(image)
		self.connect('button-press-event', self.button_press)
		self.set_tooltip_markup('<b>' + _('Empthy pattern') + '</b>')

	def button_press(self, *args):
		event = args[1]
		if event.button == 1:
			self.app.proxy.fill_selected([])
		if event.button == 3:
			self.app.proxy.stroke_selected([])

