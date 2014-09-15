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

import gtk, math

from uc2.uc2const import unit_dict, point_dict
from uc2 import uc2const

from sk1 import config, events
from sk1.appconst import KEY_KP_ENTER, KEY_RETURN


class UnitLabel(gtk.Label):

	def __init__(self):
		gtk.Label.__init__(self, config.default_unit)
		events.connect(events.CONFIG_MODIFIED, self.update_label)

	def update_label(self, *args):
		if args[0][0] == 'default_unit':
			self.set_text(config.default_unit)

class UnitSpin(gtk.SpinButton):

	point_value = 0
	flag = False
	callback = None

	def __init__(self, callback):
		#value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0
		self.callback = callback
		self.adj = gtk.Adjustment(0.0, 0.0, 1.0, 0.001, 1.0, 0.0)
		gtk.SpinButton.__init__(self, self.adj, 0.1, 2)
		self.update_increment()
		self.set_numeric(True)
		events.connect(events.CONFIG_MODIFIED, self.update_spin)
		self.connect('value-changed', self.update_point_value)

	def update_increment(self):
		self.flag = True
		if config.default_unit == uc2const.UNIT_IN:
			value = 0.001
			self.set_digits(3)
		else:
			value = 0.01
			self.set_digits(2)
		self.adj.set_upper(100000.0 * point_dict[config.default_unit])
		self.adj.set_step_increment(value)
		self.adj.set_page_increment(value)
		self.flag = True
		self.adj.set_value(self.point_value * point_dict[config.default_unit])
		self.flag = False


	def update_spin(self, *args):
		if args[0][0] == 'default_unit':
			self.update_increment()

	def update_point_value(self, *args):
		if self.flag:
			self.flag = False
		else:
			value = self.adj.get_value()
			self.point_value = value * unit_dict[config.default_unit]
			self.callback()

	def set_point_value(self, value=0.0):
		self.point_value = value
		self.flag = True
		self.adj.set_value(value * point_dict[config.default_unit])
		self.flag = False

	def get_point_value(self):
		return self.point_value

class AngleSpin(gtk.SpinButton):

	angle_value = 0
	flag = False
	callback = None
	changes = False
	input_flag = False

	def __init__(self, callback, input_flag=False):
		#value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0
		self.callback = callback
		self.input_flag = input_flag
		self.adj = gtk.Adjustment(0.0, -1000.0, 1000.0, 5.0, 5.0, 0.0)
		gtk.SpinButton.__init__(self, self.adj, 0.1, 2)
		self.set_numeric(True)
		self.connect('value-changed', self.update_angle_value)
		if self.input_flag:
			self.connect('key_press_event', self.check_input)

	def check_input(self, widget, event):
		keyval = event.keyval
		if keyval in [KEY_RETURN, KEY_KP_ENTER]:
			if self.adj.get_value() == round(self.angle_value * 180 / math.pi, 2):
				self.update_angle_value()

	def update_angle_value(self, *args):
		if self.flag:return
		value = self.adj.get_value()
		self.angle_value = math.pi * value / 180.0
		self.changes = False
		self.callback()

	def set_angle_value(self, value=0.0):
		self.angle_value = value
		self.flag = True
		self.adj.set_value(value * 180 / math.pi)
		self.flag = False

	def get_angle_value(self):
		return self.angle_value
