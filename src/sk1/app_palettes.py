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

from sk1 import _, rc, config

STD_CMYK_PALETTE = _('Standard CMYK palette')
STD_RGB_PALETTE = _('Standard RGB palette')

class SK1Palette:

	name = ''
	colors = ''

	def __init__(self, name='', colors=[]):
		self.name = name
		self.colors = colors

class AppPaletteManager:

	palette_in_use = None
	palettes = {}

	def __init__(self, app):
		self.app = app
		self.init_builtin_palettes()
		self.scan_palettes()
		self.set_palette(config.palette_in_use)

	def init_builtin_palettes(self):
		name = STD_CMYK_PALETTE
		self.palettes[name] = SK1Palette(name, rc.palette_cmyk)
		name = STD_RGB_PALETTE
		self.palettes[name] = SK1Palette(name, rc.palette_rgb)

	def scan_palettes(self): pass

	def set_palette(self, name):
		if name and name in self.palettes.keys():
			self.palette_in_use = self.palettes[name]
		else:
			self.palette_in_use = self.palettes[STD_CMYK_PALETTE]
		config.palette_in_use = self.palette_in_use.name
