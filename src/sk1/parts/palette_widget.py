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

import wal

from uc2 import uc2const
from sk1 import events, config, rc

SHIFT = 15

class HPaletteWidget(wal.CairoCanvas):

	last_color = None

	def __init__(self, master, app):
		self.app = app
		size = (-1, config.hpalette_cell_vertical)
		wal.CairoCanvas.__init__(self, master, size, has_tooltip=True)
		self.position = 0
		self.max_pos = 0
		self.max_position()
		events.connect(events.CMS_CHANGED, self.repaint_request)

	def max_position(self):
		pal = self.app.palette_mngr.palette_in_use.colors
		w, h = self.get_size()
		if w and h:
			size = float(config.hpalette_cell_horizontal)
			self.max_pos = len(pal) * size / w - 1.0
			self.max_pos *= w / size

	def update_tooltip(self, x, y):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.hpalette_cell_horizontal
		cell = int(float(x) / float(offset) - self.position)
		if cell > len(pal): return ()
		color = pal[cell]
		if not color == self.last_color:
			self.last_color = color
			return ()
		icon = fist = second = ''

		if color[3]: fist = color[3]
		val = color[1]
		if color[0] == uc2const.COLOR_CMYK:
			icon = rc.IMG_PALETTE_CMYK_COLOR
			second = 'C-%i%% M-%i%% Y-%i%% K-%i%%' % (val[0] * 100,
							val[1] * 100, val[2] * 100, val[3] * 100)

		if color[0] == uc2const.COLOR_RGB:
			icon = rc.IMG_PALETTE_RGB_COLOR
			second = 'R-%i G-%i B-%i' % (val[0] * 255, val[1] * 255, val[2] * 255)
		return (icon, fist, second)

	def mouse_wheel(self, event):
		self.position += SHIFT * event.direction
		if self.position > 0: self.position = 0
		if self.position < -self.max_pos: self.position = -self.max_pos
		self.repaint_request()

	def mouse_left_down(self, event):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.hpalette_cell_horizontal
		cell = int(float(event.pos[0]) / float(offset) - self.position)
		self.app.proxy.fill_selected(pal[cell])

	def mouse_right_down(self, event):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.hpalette_cell_horizontal
		cell = int(float(event.pos[0]) / float(offset) - self.position)
		self.app.proxy.stroke_selected(pal[cell])

	def repaint(self):
		self.max_position()
		if self.position < -self.max_pos:
			self.position = -self.max_pos
		w = self.get_size()[0]

		x0 = 0.0; y0 = 2.0
		offset = config.hpalette_cell_horizontal
		pal = self.app.palette_mngr.palette_in_use.colors
		y1 = config.hpalette_cell_vertical + 1
		self.set_antialias(False)

		i = self.position
		for color in pal:
			x0 = i * offset
			if x0 > w:break
			rect = (x0, y0, offset, y1)
			color = self.app.default_cms.get_display_color(color)
			self.rectangle(rect, color, wal.BLACK)
			i += 1

class VPaletteWidget(wal.CairoCanvas):

	last_color = None

	def __init__(self, master, app):
		self.app = app
		size = (config.vpalette_cell_horizontal, -1)
		wal.CairoCanvas.__init__(self, master, size, has_tooltip=True)
		self.position = 0
		self.max_pos = 0
		self.max_position()
		events.connect(events.CMS_CHANGED, self.repaint_request)

	def max_position(self):
		pal = self.app.palette_mngr.palette_in_use.colors
		w, h = self.get_size()
		if w and h:
			size = float(config.vpalette_cell_vertical)
			self.max_pos = len(pal) * size / h - 1.0
			self.max_pos *= h / size

	def update_tooltip(self, x, y):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.vpalette_cell_vertical
		cell = int(float(y) / float(offset) - self.position)
		if cell > len(pal): return ()
		color = pal[cell]
		if not color == self.last_color:
			self.last_color = color
			return ()
		icon = fist = second = ''

		if color[3]: fist = color[3]
		val = color[1]
		if color[0] == uc2const.COLOR_CMYK:
			icon = rc.IMG_PALETTE_CMYK_COLOR
			second = 'C-%i%% M-%i%% Y-%i%% K-%i%%' % (val[0] * 100,
							val[1] * 100, val[2] * 100, val[3] * 100)

		if color[0] == uc2const.COLOR_RGB:
			icon = rc.IMG_PALETTE_RGB_COLOR
			second = 'R-%i G-%i B-%i' % (val[0] * 255, val[1] * 255, val[2] * 255)
		return (icon, fist, second)

	def mouse_wheel(self, event):
		self.position += SHIFT * event.direction
		if self.position > 0: self.position = 0
		if self.position < -self.max_pos: self.position = -self.max_pos
		self.repaint_request()

	def mouse_left_down(self, event):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.vpalette_cell_vertical
		cell = int(float(event.pos[1]) / float(offset) - self.position)
		self.app.proxy.fill_selected(pal[cell])

	def mouse_right_down(self, event):
		pal = self.app.palette_mngr.palette_in_use.colors
		offset = config.vpalette_cell_vertical
		cell = int(float(event.pos[1]) / float(offset) - self.position)
		self.app.proxy.stroke_selected(pal[cell])

	def repaint(self):
		self.max_position()
		if self.position < -self.max_pos:
			self.position = -self.max_pos
		h = self.get_size()[1]

		x0 = 2.0; y0 = 0.0
		offset = config.vpalette_cell_vertical
		pal = self.app.palette_mngr.palette_in_use.colors
		x1 = config.vpalette_cell_horizontal
		self.set_antialias(False)

		i = self.position
		for color in pal:
			y0 = i * offset
			if y0 > h:break
			rect = (x0, y0, x1, offset)
			color = self.app.default_cms.get_display_color(color)
			self.rectangle(rect, color, wal.BLACK)
			i += 1

