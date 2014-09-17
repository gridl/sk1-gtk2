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

import gtk

from sk1 import _, actions, rc
from sk1.widgets import ActionButton, AngleSpin, ActionToggleButton
from sk1.widgets import ImageLabel

class ActionPlugin(gtk.HBox):

	def __init__(self, mw):
		gtk.HBox.__init__(self)
		self.mw = mw
		self.app = mw.app
		self.actions = self.app.actions
		self.sep = gtk.VSeparator()
		self.pack_end(self.sep, False, False, 2)
		self.build()

	def build(self):pass

class GroupPlugin(ActionPlugin):

	name = 'GroupPlugin'

	def build(self):
		self.rot_left = ActionButton(self.actions[actions.GROUP])
		self.pack_start(self.rot_left, False, False, 0)

		self.rot_left = ActionButton(self.actions[actions.UNGROUP])
		self.pack_start(self.rot_left, False, False, 0)

		self.rot_left = ActionButton(self.actions[actions.UNGROUP_ALL])
		self.pack_start(self.rot_left, False, False, 0)

class RotatePlugin(ActionPlugin):

	name = 'RotatePlugin'

	def build(self):
		self.pack_start(ImageLabel(rc.IMG_CTX_ROTATE,
								_('Rotate selection')), False, False, 2)

		self.angle_spin = AngleSpin(self.user_update, True)
		self.pack_start(self.angle_spin, False, False, 0)
		self.angle_spin.set_angle_value(0.0)

		self.rot_left = ActionButton(self.actions[actions.ROTATE_LEFT])
		self.pack_start(self.rot_left, False, False, 0)

		self.rot_right = ActionButton(self.actions[actions.ROTATE_RIGHT])
		self.pack_start(self.rot_right, False, False, 0)

	def user_update(self, *args):
		val = self.angle_spin.get_angle_value()
		if val <> 0.0:
			self.app.current_doc.api.rotate_selected(val)
			self.angle_spin.grab_focus()


class MirrorPlugin(ActionPlugin):

	name = 'MirrorPlugin'

	def build(self):
		self.rot_left = ActionButton(self.actions[actions.HOR_MIRROR])
		self.pack_start(self.rot_left, False, False, 0)

		self.rot_right = ActionButton(self.actions[actions.VERT_MIRROR])
		self.pack_start(self.rot_right, False, False, 0)

class CombinePlugin(ActionPlugin):

	name = 'CombinePlugin'

	def build(self):
		self.rot_left = ActionButton(self.actions[actions.COMBINE])
		self.pack_start(self.rot_left, False, False, 0)

		self.rot_right = ActionButton(self.actions[actions.BREAK_APART])
		self.pack_start(self.rot_right, False, False, 0)

class ToCurvePlugin(ActionPlugin):

	name = 'ToCurvePlugin'

	def build(self):
		self.but = ActionButton(self.actions[actions.CONVERT_TO_CURVES])
		self.pack_start(self.but, False, False, 0)

class SnappingPlugin(ActionPlugin):

	name = 'SnappingPlugin'

	def build(self):
		self.but = ActionToggleButton(self.actions[actions.SNAP_TO_GRID])
		self.pack_start(self.but, False, False, 0)

		self.but = ActionToggleButton(self.actions[actions.SNAP_TO_GUIDES])
		self.pack_start(self.but, False, False, 0)

		self.but = ActionToggleButton(self.actions[actions.SNAP_TO_OBJECTS])
		self.pack_start(self.but, False, False, 0)

		self.but = ActionToggleButton(self.actions[actions.SNAP_TO_PAGE])
		self.pack_start(self.but, False, False, 0)

class PageBorderPlugin(ActionPlugin):

	name = 'PageBorderPlugin'

	def build(self):
		self.but = ActionButton(self.actions[actions.PAGE_FRAME])
		self.pack_start(self.but, False, False, 0)
		self.but = ActionButton(self.actions[actions.PAGE_GUIDE_FRAME])
		self.pack_start(self.but, False, False, 0)
		self.but = ActionButton(self.actions[actions.GUIDES_AT_CENTER])
		self.pack_start(self.but, False, False, 0)
		self.but = ActionButton(self.actions[actions.REMOVE_ALL_GUIDES])
		self.pack_start(self.but, False, False, 0)

