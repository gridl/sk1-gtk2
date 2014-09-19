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

from sk1.widgets import VBox, HBox, HLine
from sk1.ui.ctxtoolbar import CtxToolBar

class WorkingArea(VBox):

	def __init__(self, mw):
		self.mw = mw
		self.app = mw.app
		VBox.__init__(self)

		self.ctxtb = CtxToolBar(self.mw)
		self.pack_start(self.ctxtb, False, True)
		self.pack_start(HLine(), fill=True)

		self.box = HBox()

		#here should be WA content

		self.pack_start(self.box, True, True)

