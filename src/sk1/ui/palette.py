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

from sk1 import _, const, rc, config
from sk1.parts import HPaletteWidget, VPaletteWidget

class PaletteTemplate:

	pw = None

	def action_dforward(self, *args):
		self.pw.position -= 20
		if self.pw.position < -self.pw.max_pos:
			self.pw.position = -self.pw.max_pos
		self.pw.repaint_request()

	def action_forward(self, *args):
		self.pw.position -= 1
		if self.pw.position < -self.pw.max_pos:
			self.pw.position = -self.pw.max_pos
		self.pw.repaint_request()

	def action_back(self, *args):
		self.pw.position += 1
		if self.pw.position > 0:
			self.pw.position = 0
		self.pw.repaint_request()

	def action_dback(self, *args):
		self.pw.position += 20
		if self.pw.position > 0:
			self.pw.position = 0
		self.pw.repaint_request()

	def action_nocolor(self, button):
		if button == const.LEFT_BUTTON:
			self.app.proxy.fill_selected([])
		if button == const.RIGHT_BUTTON:
			self.app.proxy.stroke_selected([])


class HPalette(wal.HidableVBox, PaletteTemplate):

	def __init__(self, master, app):
		self.app = app
		wal.HidableVBox.__init__(self, master)

		self.pack(wal.HLine(self), padding=1)

		box = wal.HBox(self)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_LEFT,
						cmd=self.action_dback, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_LEFT,
						cmd=self.action_back, repeat=True, flat=True))

		box.pack(wal.ClickableImage(self, rc.IMG_PALETTE_NO_COLOR,
				tooltip=_('Empthy pattern'), cmd=self.action_nocolor))

		self.pw = HPaletteWidget(box, self.app)
		box.pack(self.pw, True, True, 1)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_RIGHT,
						cmd=self.action_forward, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_RIGHT,
						cmd=self.action_dforward, repeat=True, flat=True))
		self.pack(box, True, True)

		if config.palette_orientation == const.HORIZONTAL and  config.palette_visible:
			self.set_visible(True)
		else:
			self.set_visible(False)



class VPalette(wal.HidableHBox, PaletteTemplate):

	def __init__(self, master, app):
		self.app = app
		wal.HidableHBox.__init__(self, master)

		self.pack(wal.VLine(self), padding=1)

		box = wal.VBox(self)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_TOP,
						cmd=self.action_dback, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_TOP,
						cmd=self.action_back, repeat=True, flat=True))

		box.pack(wal.ClickableImage(self, rc.IMG_PALETTE_NO_COLOR,
				tooltip=_('Empthy pattern'), cmd=self.action_nocolor))

		self.pw = VPaletteWidget(box, self.app)
		box.pack(self.pw, True, True, 1)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_BOTTOM,
						cmd=self.action_forward, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_BOTTOM,
						cmd=self.action_dforward, repeat=True, flat=True))
		self.pack(box, True, True)

		if config.palette_orientation == const.VERTICAL and  config.palette_visible:
			self.set_visible(True)
		else:
			self.set_visible(False)

