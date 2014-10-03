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

from sk1 import _, events, rc
from sk1.parts import UnitLabel, UnitSpin, KeepRatioLabel
from sk1.context.generic import GenericPlugin

class ResizePlugin(GenericPlugin):

	name = 'ResizePlugin'


	def __init__(self, app, master):
		GenericPlugin.__init__(self, app, master)
		events.connect(events.NO_DOCS, self.set_state)
		events.connect(events.DOC_CHANGED, self.set_state)
		events.connect(events.SELECTION_CHANGED, self.set_state)

	def build(self):
		self.pack(wal.Label(self, _('Size:')), padding=2)

		self.width_spin = UnitSpin(self, self.user_changes)
		self.pack(self.width_spin)

		self.pack(wal.Image(self, rc.IMG_CTX_W_ON_H))

		self.height_spin = UnitSpin(self, self.user_changes)
		self.pack(self.height_spin)

		self.pack(UnitLabel(self), padding=2)

		self.keep_ratio = KeepRatioLabel(self)
		self.pack(self.keep_ratio, padding=5)

	def set_state(self, *args):
		if self.app.current_doc is None:
			self.deactivate()
		else:
			if self.app.current_doc.selection.objs:
				self.activate()
			else:
				self.deactivate()

	def deactivate(self):
		self.width_spin.set_point_value(0)
		self.height_spin.set_point_value(0)
		self.set_sensitive(False)

	def activate(self):
		bbox = self.app.current_doc.selection.bbox
		w = bbox[2] - bbox[0]
		h = bbox[3] - bbox[1]
		self.width_spin.set_point_value(w)
		self.height_spin.set_point_value(h)
		self.set_sensitive(True)

	def user_changes(self, *args):
		doc = self.app.current_doc
		if not doc is None and doc.selection.objs:
			bbox = doc.selection.bbox
			w = bbox[2] - bbox[0]
			h = bbox[3] - bbox[1]
			center_x = bbox[0] + w / 2.0
			center_y = bbox[1] + h / 2.0

			new_w = self.width_spin.get_point_value()
			new_h = self.height_spin.get_point_value()

			if not round(w, 4) == round(new_w, 4) or not round(h, 4) == round(new_h, 4):
				if not new_w: self.width_spin.set_point_value(w);return
				if not new_h: self.height_spin.set_point_value(h);return

				m11 = round(new_w / w, 4)
				m22 = round(new_h / h, 4)

				if m11 == m22 == 1.0:return

				trafo = []

				if self.keep_ratio.value:
					if m11 == 1.0:
						dx = center_x * (1 - m22)
						dy = center_y * (1 - m22)
						trafo = [m22, 0.0, 0.0, m22, dx, dy]
					if m22 == 1.0:
						dx = center_x * (1 - m11)
						dy = center_y * (1 - m11)
						trafo = [m11, 0.0, 0.0, m11, dx, dy]
				else:
					dx = center_x * (1 - m11)
					dy = center_y * (1 - m22)
					trafo = [m11, 0.0, 0.0, m22, dx, dy]

				if trafo:
					doc.api.transform_selected(trafo)
