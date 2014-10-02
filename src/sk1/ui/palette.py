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

from sk1 import _, const, rc
from sk1.parts import HPaletteWidget

class PaletteTemplate:

	pw = None

	def action_dforward(self, *args):
		self.pw.position -= 20
		if self.pw.position < -self.pw.max_pos:
			self.pw.position = -self.pw.max_pos
		self.pw.queue_draw()

	def action_forward(self, *args):
		self.pw.position -= 1
		if self.pw.position < -self.pw.max_pos:
			self.pw.position = -self.pw.max_pos
		self.pw.queue_draw()

	def action_back(self, *args):
		self.pw.position += 1
		if self.pw.position > 0:
			self.pw.position = 0
		self.pw.queue_draw()

	def action_dback(self, *args):
		self.pw.position += 20
		if self.pw.position > 0:
			self.pw.position = 0
		self.pw.queue_draw()

	def action_nocolor(self, button):
		if button == const.LEFT_BUTTON:
			self.app.proxy.fill_selected([])
		if button == const.RIGHT_BUTTON:
			self.app.proxy.stroke_selected([])


class HPalette(wal.HidableVBox, PaletteTemplate):

	def __init__(self, app, master):
		self.app = app
		wal.HidableVBox.__init__(self, master)

		self.pack(wal.HLine(self))

		box = wal.HBox(self)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_LEFT,
						cmd=self.action_dback, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_LEFT,
						cmd=self.action_back, repeat=True, flat=True))

		box.pack(wal.ActiveImage(self, rc.IMG_PALETTE_NO_COLOR,
				tooltip=_('Empthy pattern'), cmd=self.action_nocolor))

		self.pw = HPaletteWidget(self.app)
		box.pack(self.pw, True, True, 1)

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_ARROW_RIGHT,
						cmd=self.action_forward, repeat=True, flat=True))

		box.pack(wal.ImgButton(self, rc.IMG_PALETTE_DOUBLE_ARROW_RIGHT,
						cmd=self.action_dforward, repeat=True, flat=True))
		self.pack(box, True, True)

