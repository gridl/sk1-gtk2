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

from sk1 import _, config, events
from sk1.context.transform import GroupPlugin, MirrorPlugin, RotatePlugin, \
ToCurvePlugin, CombinePlugin, SnappingPlugin, PageBorderPlugin
from sk1.context.units import UnitsPlugin
from sk1.context.resize import ResizePlugin
from sk1.context.page_format import PageFormatPlugin
from sk1.context.jump import JumpPlugin

PLUGINS = [UnitsPlugin, GroupPlugin, MirrorPlugin, RotatePlugin, ResizePlugin,
		PageFormatPlugin, ToCurvePlugin, JumpPlugin, CombinePlugin, SnappingPlugin,
		PageBorderPlugin, ]

NO_DOC = []
DEFAULT = ['PageFormatPlugin', 'UnitsPlugin', 'JumpPlugin', 'SnappingPlugin', 'PageBorderPlugin']
MULTIPLE = ['ResizePlugin', 'GroupPlugin', 'CombinePlugin', 'RotatePlugin', 'MirrorPlugin', 'ToCurvePlugin' ]
GROUP = ['ResizePlugin', 'GroupPlugin', 'RotatePlugin', 'MirrorPlugin', 'SnappingPlugin']
RECTANGLE = ['ResizePlugin', 'RotatePlugin', 'MirrorPlugin', 'ToCurvePlugin', 'SnappingPlugin']
CIRCLE = ['ResizePlugin', 'RotatePlugin', 'MirrorPlugin', 'ToCurvePlugin', 'SnappingPlugin']
POLYGON = ['ResizePlugin', 'RotatePlugin', 'MirrorPlugin', 'ToCurvePlugin', 'SnappingPlugin']
CURVE = ['ResizePlugin', 'CombinePlugin', 'RotatePlugin', 'MirrorPlugin', 'SnappingPlugin']
TEXT = []
PIXMAP = []


class ContextPanel(wal.HBox):

	plugins_dict = {}
	plugins = []

	def __init__(self, app, master):
		wal.HBox.__init__(self, master)

		self.app = app
		self.mw = app.mw
		self.insp = self.app.inspector

		for item in PLUGINS:
			plg = item(self.mw)
			self.plugins_dict[plg.name] = plg

		events.connect(events.NO_DOCS, self.rebuild)
		events.connect(events.DOC_CHANGED, self.rebuild)
		events.connect(events.SELECTION_CHANGED, self.rebuild)
		self.rebuild()

	def rebuild(self, *args):
		for item in self.plugins:
			self.remove(item)
		self.plugins = []
		mode = self.get_mode()
		if mode:
			for item in mode:
				self.pack(self.plugins_dict[item])
				self.plugins.append(self.plugins_dict[item])
				self.plugins_dict[item].show_all()

	def get_mode(self):
		if not self.insp.is_doc():
			return NO_DOC
		if not self.insp.is_selection():
			return DEFAULT
		else:
			doc = self.app.current_doc
			sel = doc.selection.objs
			if len(sel) > 1:
				return MULTIPLE
			elif self.insp.is_obj_rect(sel[0]):
				return RECTANGLE
			elif self.insp.is_obj_circle(sel[0]):
				return CIRCLE
			elif self.insp.is_obj_polygon(sel[0]):
				return POLYGON
			elif self.insp.is_obj_curve(sel[0]):
				return CURVE
			elif self.insp.can_be_ungrouped():
				return GROUP
			else:
				return DEFAULT




