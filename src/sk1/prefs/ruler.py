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

import gtk

from sk1 import _, config, rc
from sk1.prefs.generic import GenericPrefsPlugin
from sk1.widgets import SpinButtonInt, ColorButton

class RulerPlugin(GenericPrefsPlugin):

	name = 'RulerPlugin'
	title = _('Ruler Preferences')
	short_title = _('Ruler')
	image_id = rc.IMG_PREFS_RULER

	def __init__(self, app, dlg, fmt_config):
		GenericPrefsPlugin.__init__(self, app, dlg, fmt_config)

	def build(self):
		GenericPrefsPlugin.build(self)

		tab = gtk.Table(1, 1, False)
		tab.set_row_spacings(5)
		tab.set_col_spacings(10)
		tab.set_border_width(5)

		#--- Ruler size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler size (px):')))
		tab.attach(al, 0, 1, 0, 1, gtk.FILL , gtk.SHRINK)

		self.size_spin = SpinButtonInt(config.ruler_size, (15, 30))
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.size_spin)
		tab.attach(al, 1, 2, 0, 1, gtk.FILL, gtk.SHRINK)

		#--- Ruler font size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler font size (px):')))
		tab.attach(al, 0, 1, 1, 2, gtk.FILL , gtk.SHRINK)

		self.fsize_spin = SpinButtonInt(config.ruler_font_size, (5, 8))
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.fsize_spin)
		tab.attach(al, 1, 2, 1, 2, gtk.FILL, gtk.SHRINK)

		#--- Background color
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler background color:')))
		tab.attach(al, 0, 1, 2, 3, gtk.FILL, gtk.SHRINK)

		self.bgcolor = ColorButton(config.ruler_bgcolor)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.bgcolor)
		tab.attach(al, 1, 2, 2, 3, gtk.FILL, gtk.SHRINK)

		#--- Foreground color
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler tick color:')))
		tab.attach(al, 0, 1, 3, 4, gtk.FILL, gtk.SHRINK)

		self.fgcolor = ColorButton(config.ruler_fgcolor)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.fgcolor)
		tab.attach(al, 1, 2, 3, 4, gtk.FILL, gtk.SHRINK)

		#--- Small tick size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Small tick size (px):')))
		tab.attach(al, 0, 1, 4, 5, gtk.FILL , gtk.SHRINK)

		self.stick_spin = SpinButtonInt(config.ruler_small_tick, (1, 30))
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.stick_spin)
		tab.attach(al, 1, 2, 4, 5, gtk.FILL, gtk.SHRINK)

		#--- Large tick size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Large tick size (px):')))
		tab.attach(al, 0, 1, 5, 6, gtk.FILL , gtk.SHRINK)

		self.ltick_spin = SpinButtonInt(config.ruler_text_tick, (1, 30))
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.ltick_spin)
		tab.attach(al, 1, 2, 5, 6, gtk.FILL, gtk.SHRINK)

		#--- Text mark shift
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Text mark shift (px):')))
		tab.attach(al, 0, 1, 6, 7, gtk.FILL , gtk.SHRINK)

		self.tmshift_spin = SpinButtonInt(config.ruler_text_shift, (-30, 30))
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.tmshift_spin)
		tab.attach(al, 1, 2, 6, 7, gtk.FILL, gtk.SHRINK)


		self.pack_start(tab, False, False, 0)

	def apply_changes(self):
		config.ruler_size = self.size_spin.get_value()
		config.ruler_font_size = self.fsize_spin.get_value()
		config.ruler_bgcolor = self.bgcolor.get_color()
		config.ruler_fgcolor = self.fgcolor.get_color()
		config.ruler_small_tick = self.stick_spin.get_value()
		config.ruler_text_tick = self.ltick_spin.get_value()
		config.ruler_text_shift = self.tmshift_spin.get_value()

	def restore_defaults(self):
		defaults = config.get_defaults()
		self.size_spin.set_value(defaults['ruler_size'])
		self.fsize_spin.set_value(defaults['ruler_font_size'])
		self.bgcolor.set_color(defaults['ruler_bgcolor'])
		self.fgcolor.set_color(defaults['ruler_fgcolor'])
		self.stick_spin.set_value(defaults['ruler_small_tick'])
		self.ltick_spin.set_value(defaults['ruler_text_tick'])
		self.tmshift_spin.set_value(defaults['ruler_text_shift'])
