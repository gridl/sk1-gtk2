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

import math, wal

from uc2.uc2const import unit_dict, point_dict
from uc2 import uc2const

from sk1 import config, events


class UnitLabel(wal.Label):

	def __init__(self, master):
		wal.Label.__init__(self, master, config.default_unit)
		events.connect(events.CONFIG_MODIFIED, self.update_label)

	def update_label(self, *args):
		if args[0][0] == 'default_unit':
			self.set_text(config.default_unit)

class UnitSpin(wal.SpinButton):

	point_value = 0
	callback = None

	def __init__(self, master, callback):
		self.callback = callback
		wal.SpinButton.__init__(self, master, cmd=self._update_point_value,
							check_focus=True)
		self.update_increment()
		events.connect(events.CONFIG_MODIFIED, self._update_spin)

	def _update_spin(self, *args):
		if args[0][0] == 'default_unit':
			self.update_increment()

	def _update_point_value(self, *args):
		value = self.get_value()
		self.point_value = value * unit_dict[config.default_unit]
		self.callback()

	def update_increment(self):
		if config.default_unit in [uc2const.UNIT_IN, uc2const.UNIT_FT,
								uc2const.UNIT_M]:
			value = 0.001
			self.set_digits(3)
		else:
			value = 0.01
			self.set_digits(2)
		self.set_upper(100000.0 * point_dict[config.default_unit])
		self.set_step_increment(value)
		self.set_page_increment(value)
		self.set_value(self.point_value * point_dict[config.default_unit])

	def set_point_value(self, value=0.0):
		self.point_value = value
		self.set_value(value * point_dict[config.default_unit])

	def get_point_value(self):
		return self.point_value

class AngleSpin(wal.SpinButton):

	angle_value = 0.0
	callback = None

	def __init__(self, master, callback):
		self.callback = callback
		wal.SpinButton.__init__(self, master, cmd=self.update_angle_value)
		self.set_range((-1000.0, 1000.0))
		self.set_step_increment(5.0)
		self.set_page_increment(5.0)
		self.set_digits(1)

	def update_angle_value(self, *args):
		value = self.get_value()
		self.angle_value = math.pi * value / 180.0
		self.callback()

	def set_angle_value(self, value=0.0):
		self.angle_value = value
		self.set_value(value * 180 / math.pi)

	def get_angle_value(self):
		return self.angle_value

