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

import gtk, os, cairo, wal

from sk1 import _, config, rc, const
from sk1.prefs.generic import GenericPrefsPlugin
from sk1.widgets import SpinButtonInt

class RulerPlugin(GenericPrefsPlugin):

	name = 'RulerPlugin'
	title = _('Ruler Preferences')
	short_title = _('Ruler')
	image_id = rc.IMG_PREFS_RULER

	def __init__(self, app, dlg, fmt_config):
		GenericPrefsPlugin.__init__(self, app, dlg, fmt_config)

	def build(self):
		GenericPrefsPlugin.build(self)

		self.test_ruler = TestRuler(self)

		tab = gtk.Table(1, 1, False)
		tab.set_row_spacings(5)
		tab.set_col_spacings(10)
		tab.set_border_width(5)

		#--- Ruler size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler size (px):')))
		tab.attach(al, 0, 1, 0, 1, gtk.FILL , gtk.SHRINK)

		self.size_spin = SpinButtonInt(config.ruler_size, (15, 30),
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.size_spin)
		tab.attach(al, 1, 2, 0, 1, gtk.FILL, gtk.SHRINK)

		#--- Ruler font size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler font size (px):')))
		tab.attach(al, 0, 1, 1, 2, gtk.FILL , gtk.SHRINK)

		self.fsize_spin = SpinButtonInt(config.ruler_font_size, (5, 8),
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.fsize_spin)
		tab.attach(al, 1, 2, 1, 2, gtk.FILL, gtk.SHRINK)

		#--- Background color
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler background color:')))
		tab.attach(al, 0, 1, 2, 3, gtk.FILL, gtk.SHRINK)

		self.bgcolor = wal.ColorButton(tab, config.ruler_bgcolor,
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.bgcolor)
		tab.attach(al, 1, 2, 2, 3, gtk.FILL, gtk.SHRINK)

		#--- Foreground color
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Ruler tick color:')))
		tab.attach(al, 0, 1, 3, 4, gtk.FILL, gtk.SHRINK)

		self.fgcolor = wal.ColorButton(tab, config.ruler_fgcolor,
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.fgcolor)
		tab.attach(al, 1, 2, 3, 4, gtk.FILL, gtk.SHRINK)

		#--- Small tick size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Small tick size (px):')))
		tab.attach(al, 0, 1, 4, 5, gtk.FILL , gtk.SHRINK)

		self.stick_spin = SpinButtonInt(config.ruler_small_tick, (1, 30),
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.stick_spin)
		tab.attach(al, 1, 2, 4, 5, gtk.FILL, gtk.SHRINK)

		#--- Large tick size
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Large tick size (px):')))
		tab.attach(al, 0, 1, 5, 6, gtk.FILL , gtk.SHRINK)

		self.ltick_spin = SpinButtonInt(config.ruler_text_tick, (1, 30),
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.ltick_spin)
		tab.attach(al, 1, 2, 5, 6, gtk.FILL, gtk.SHRINK)

		#--- Text mark shift
		al = gtk.Alignment(1.0, 0.5)
		al.add(gtk.Label(_('Text mark shift (px):')))
		tab.attach(al, 0, 1, 6, 7, gtk.FILL , gtk.SHRINK)

		self.tmshift_spin = SpinButtonInt(config.ruler_text_shift, (-30, 30),
									cmd=self.test_ruler.redraw)
		al = gtk.Alignment(0.0, 0.5)
		al.add(self.tmshift_spin)
		tab.attach(al, 1, 2, 6, 7, gtk.FILL, gtk.SHRINK)


		self.pack_start(tab, False, False, 0)

		#--- Testing ruler
		al = wal.DecorLabel(self, _('Testing ruler:'), bold=True)
		self.pack_start(al, False, False, 20)

		self.pack_start(gtk.HSeparator(), False, False, 0)
		self.pack_start(self.test_ruler, False, False, 0)

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
		self.test_ruler.redraw()


SMALL_TICKS = [15.017, 34.373, 53.729, 73.085, 92.441, 111.797, 131.153,
150.509, 169.865, 189.221, 208.577, 227.933, 247.289, 266.645, 286.001,
305.357, 324.714, 344.070, ]

TEXT_TICKS = [(15.017, '-100'), (53.729, '-75'), (92.441, '-50'),
(131.153, '-25'), (169.865, '0'), (208.577, '25'),
(247.289, '50'), (286.001, '75'), (324.714, '100'), ]

HFONT = {}
VFONT = {}

def load_font(ruler_font_size):
	fntdir = 'ruler-font%dpx' % (ruler_font_size,)
	fntdir = os.path.join(config.resource_dir, 'fonts', fntdir)
	for char in '.,-0123456789':
		if char in '.,': file_name = os.path.join(fntdir, 'hdot.png')
		else: file_name = os.path.join(fntdir, 'h%s.png' % char)
		surface = cairo.ImageSurface.create_from_png(file_name)
		HFONT[char] = (surface.get_width(), surface)

		if char in '.,': file_name = os.path.join(fntdir, 'vdot.png')
		else: file_name = os.path.join(fntdir, 'v%s.png' % char)
		surface = cairo.ImageSurface.create_from_png(file_name)
		VFONT[char] = (surface.get_height(), surface)

class TestRuler(gtk.DrawingArea):

	width = 345
	height = 20
	font_size = config.ruler_font_size
	surface = None

	def __init__(self, plg):
		self.plg = plg
		gtk.DrawingArea.__init__(self)
		self.height = config.ruler_size
		self.font_size = config.ruler_font_size
		if not VFONT: load_font(self.font_size)
		self.set_size_request(-1, self.height)
		self.connect(const.EVENT_EXPOSE, self.repaint)

	def redraw(self, *args):
		self.queue_draw()

	def repaint(self, *args):
		ruler_size = self.plg.size_spin.get_value()
		if not self.height == ruler_size:
			self.height = ruler_size
			self.set_size_request(self.width, self.height)
			self.show()

		ruler_font_size = self.plg.fsize_spin.get_value()
		if not self.font_size == ruler_font_size:
			self.font_size = ruler_font_size
			load_font(self.font_size)

		ruler_bgcolor = self.plg.bgcolor.get_color()
		ruler_fgcolor = self.plg.fgcolor.get_color()
		ruler_text_tick = self.plg.ltick_spin.get_value()
		ruler_small_tick = self.plg.stick_spin.get_value()
		text_shift = self.plg.tmshift_spin.get_value()

		w, h = tuple(self.allocation)[2:]
		win_ctx = self.window.cairo_create()

		if self.surface is None:
			self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
			self.width = w
			self.height = h
		elif self.width <> w or self.height <> h:
			self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
			self.width = w
			self.height = h
		self.surface.set_device_offset(0, 0)
		self.ctx = cairo.Context(self.surface)
		self.ctx.set_matrix(cairo.Matrix(1.0, 0.0, 0.0, 1.0, 0.0, 0.0))
		self.ctx.set_source_rgb(*ruler_bgcolor)
		self.ctx.paint()
		self.ctx.set_antialias(cairo.ANTIALIAS_NONE)
		self.ctx.set_line_width(1.0)
		self.ctx.set_dash([])
		self.ctx.set_source_rgba(*ruler_fgcolor)

		self.ctx.move_to(0, h - 1)
		self.ctx.line_to(w, h - 1)

		for item in SMALL_TICKS:
			self.ctx.move_to(item, h - ruler_small_tick)
			self.ctx.line_to(item, h - 1)

		for pos, txt in TEXT_TICKS:
			self.ctx.move_to(pos, h - ruler_text_tick)
			self.ctx.line_to(pos, h - 1)

		self.ctx.stroke()

		shift = ruler_size - ruler_font_size - ruler_text_tick - 1
		for pos, txt in TEXT_TICKS:
			for character in txt:
				data = HFONT[character]
				self.ctx.set_source_surface(data[1],
										int(pos) + text_shift, shift)
				self.ctx.paint()
				pos += data[0]

		win_ctx.set_source_surface(self.surface)
		win_ctx.paint()
