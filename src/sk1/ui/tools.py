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

from sk1 import modes

class AppTools(wal.HidableHBox):

	def __init__(self, app, master):
		wal.HidableHBox.__init__(self, master)
		self.master = master
		self.app = app
		self.actions = self.app.actions

		vbox = wal.VBox(self)
		self.pack(vbox)
		vbox.pack(wal.VBox(vbox), padding=15)

		entries = [
			None,
			modes.SELECT_MODE ,
			modes.SHAPER_MODE ,
			modes.ZOOM_MODE ,
			modes.FLEUR_MODE ,
			modes.LINE_MODE ,
			modes.CURVE_MODE ,
			modes.RECT_MODE ,
			modes.ELLIPSE_MODE ,
#			modes.POLYGON_MODE ,
			modes.TEXT_MODE ,
			None,
			wal.IMG_TOOL_STROKE,
			wal.IMG_TOOL_FILL,
			None
		]

		for entry in entries:
			if entry is None:
				vbox.pack(wal.HLine(vbox))
			elif isinstance(entry, basestring):
				vbox.pack(wal.ImgButton(vbox, entry, flat=True))
			else:
				vbox.pack(wal.ActionToggleButton(vbox, self.actions[entry]))








