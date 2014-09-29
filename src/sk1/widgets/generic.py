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

import gtk, gconst

class SpinButton(gtk.SpinButton):

	def __init__(self, val=0.0, valrange=[0.0, 1.0], step_incr=0.1, cmd=None):
		#value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0
		self.adj = gtk.Adjustment(val, valrange[0], valrange[1], step_incr, 1.0, 0.0)
		gtk.SpinButton.__init__(self, self.adj, 0.1, 2)
		self.set_numeric(True)
		if cmd: self.connect(gconst.EVENT_VALUE_CHANGED, cmd)

class SpinButtonInt(SpinButton):

	def __init__(self, val=0, valrange=[0, 10], step_incr=1, cmd=None):
		SpinButton.__init__(self, val, valrange, step_incr, cmd)
		self.set_digits(0)

	def get_value(self):
		return self.get_value_as_int()
