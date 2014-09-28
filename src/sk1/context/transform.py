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

import wal

from sk1 import actions
from sk1.parts import AngleSpin
from sk1.context.generic import GenericPlugin

class GroupPlugin(GenericPlugin):

	name = 'GroupPlugin'

	def build(self):
		self.pack(wal.ActionButton(self, self.actions[actions.GROUP]))
		self.pack(wal.ActionButton(self, self.actions[actions.UNGROUP]))
		self.pack(wal.ActionButton(self, self.actions[actions.UNGROUP_ALL]))

class RotatePlugin(GenericPlugin):

	name = 'RotatePlugin'

	def build(self):
		self.pack(wal.ActiveImage(self, wal.IMG_CTX_ROTATE), padding=2)

		self.angle_spin = AngleSpin(self.user_update, True)
		self.pack_start(self.angle_spin, False, False, 0)
		self.angle_spin.set_angle_value(0.0)

		self.pack(wal.ActionButton(self, self.actions[actions.ROTATE_LEFT]))
		self.pack(wal.ActionButton(self, self.actions[actions.ROTATE_RIGHT]))

	def user_update(self, *args):
		val = self.angle_spin.get_angle_value()
		if val <> 0.0:
			self.app.current_doc.api.rotate_selected(val)
			self.angle_spin.grab_focus()


class MirrorPlugin(GenericPlugin):

	name = 'MirrorPlugin'

	def build(self):
		self.pack(wal.ActionButton(self, self.actions[actions.HOR_MIRROR]))
		self.pack(wal.ActionButton(self, self.actions[actions.VERT_MIRROR]))

class CombinePlugin(GenericPlugin):

	name = 'CombinePlugin'

	def build(self):
		self.pack(wal.ActionButton(self, self.actions[actions.COMBINE]))
		self.pack(wal.ActionButton(self, self.actions[actions.BREAK_APART]))

class ToCurvePlugin(GenericPlugin):

	name = 'ToCurvePlugin'

	def build(self):
		self.pack(wal.ActionButton(self, self.actions[actions.CONVERT_TO_CURVES]))

class SnappingPlugin(GenericPlugin):

	name = 'SnappingPlugin'

	def build(self):
		self.pack(wal.ActionToggleButton(self, self.actions[actions.SNAP_TO_GRID]))
		self.pack(wal.ActionToggleButton(self, self.actions[actions.SNAP_TO_GUIDES]))
		self.pack(wal.ActionToggleButton(self, self.actions[actions.SNAP_TO_OBJECTS]))
		self.pack(wal.ActionToggleButton(self, self.actions[actions.SNAP_TO_PAGE]))

class PageBorderPlugin(GenericPlugin):

	name = 'PageBorderPlugin'

	def build(self):
		self.pack(wal.ActionButton(self, self.actions[actions.PAGE_FRAME]))
		self.pack(wal.ActionButton(self, self.actions[actions.PAGE_GUIDE_FRAME]))
		self.pack(wal.ActionButton(self, self.actions[actions.GUIDES_AT_CENTER]))
		self.pack(wal.ActionButton(self, self.actions[actions.REMOVE_ALL_GUIDES]))

