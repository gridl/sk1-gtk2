# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2014 by Igor E. Novikov
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

import os, math

import gtk
import gobject
import cairo

from uc2 import uc2const
from uc2.uc2const import HORIZONTAL, VERTICAL
from uc2.formats.sk1.sk1const import DOC_ORIGIN_CENTER, DOC_ORIGIN_LU, \
DOC_ORIGIN_LL, ORIGINS

from sk1 import config, events, modes, rc, const
from sk1.const import RENDERING_DELAY

HFONT = {}
VFONT = {}

BITMAPS = {}

CAIRO_WHITE = [1.0, 1.0, 1.0]
CAIRO_BLACK = [0.0, 0.0, 0.0]

DEFAULT_CURSOR = -1

def load_font():
	fntdir = os.path.join(config.resource_dir, 'ruler-font')
	for char in '.,-0123456789':
		if char in '.,': file_name = os.path.join(fntdir, 'hdot.png')
		else: file_name = os.path.join(fntdir, 'h%s.png' % char)
		surface = cairo.ImageSurface.create_from_png(file_name)
		HFONT[char] = (surface.get_width(), surface)

		if char in '.,': file_name = os.path.join(fntdir, 'vdot.png')
		else: file_name = os.path.join(fntdir, 'v%s.png' % char)
		surface = cairo.ImageSurface.create_from_png(file_name)
		VFONT[char] = (surface.get_height(), surface)

def load_bitmaps():
	file_name = rc.get_image_path(rc.IMG_RULER_BG)
	BITMAPS['bg'] = cairo.ImageSurface.create_from_png(file_name)
	file_name = rc.get_image_path(rc.IMG_RULER_DO_C)
	BITMAPS[DOC_ORIGIN_CENTER] = cairo.ImageSurface.create_from_png(file_name)
	file_name = rc.get_image_path(rc.IMG_RULER_DO_LU)
	BITMAPS[DOC_ORIGIN_LU] = cairo.ImageSurface.create_from_png(file_name)
	file_name = rc.get_image_path(rc.IMG_RULER_DO_LL)
	BITMAPS[DOC_ORIGIN_LL] = cairo.ImageSurface.create_from_png(file_name)

class RulerCorner(gtk.DrawingArea):

	def __init__(self, docarea):
		gtk.DrawingArea.__init__(self)
		if not BITMAPS:load_bitmaps()
		self.docarea = docarea
		self.presenter = docarea.presenter
		self.eventloop = self.presenter.eventloop
		self.origin = self.presenter.model.doc_origin

		self.add_events(gtk.gdk.BUTTON_PRESS_MASK |
					gtk.gdk.BUTTON_RELEASE_MASK)

		size = config.ruler_size
		self.set_size_request(size, size)
		self.connect(const.EVENT_EXPOSE, self.repaint)
		self.connect(const.EVENT_BUTTON_RELEASE, self.click_event)
		self.eventloop.connect(self.eventloop.DOC_MODIFIED, self.check_coords)
		events.connect(events.CONFIG_MODIFIED, self.check_config)

	def close(self):
		events.disconnect(events.CONFIG_MODIFIED, self.check_config)
		fields = self.__dict__
		items = fields.keys()
		for item in items: fields[item] = None

	def check_config(self, *args):
		if args[0][0] == 'ruler_size':
			size = config.ruler_size
			if self.orient: self.set_size_request(size, -1)
			else: self.set_size_request(-1, size)
			return
		if args[0][0][:6] == 'ruler_':
			self.queue_draw()

	def check_coords(self, *args):
		if not self.origin == self.presenter.model.doc_origin:
			self.origin = self.presenter.model.doc_origin
			self.queue_draw()

	def click_event(self, *args):
		origin = self.presenter.model.doc_origin
		if origin < ORIGINS[-1]:
			origin += 1
		else:
			origin = ORIGINS[0]
		self.presenter.api.set_doc_origin(origin)

	def repaint(self, *args):
		w, h = tuple(self.allocation)[2:]
		win_ctx = self.window.cairo_create()

		surface = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
		surface.set_device_offset(0, 0)
		ctx = cairo.Context(surface)
		ctx.set_matrix(cairo.Matrix(1.0, 0.0, 0.0, 1.0, 0.0, 0.0))
		ctx.set_source_rgb(*CAIRO_WHITE)
		ctx.paint()

		bmp = BITMAPS['bg']
		ctx.set_source_surface(bmp, w - bmp.get_width(), h - bmp.get_height())
		ctx.paint()

		bmp = BITMAPS[self.origin]
		x = (w - 1 - bmp.get_width()) / 2
		y = (h - 1 - bmp.get_height()) / 2
		ctx.set_source_surface(bmp, x, y)
		ctx.paint()

		win_ctx.set_source_surface(surface)
		win_ctx.paint()

class Ruler(gtk.DrawingArea):

	exposed = False
	surface = None
	ctx = None

	def __init__(self, docarea, orient):
		gtk.DrawingArea.__init__(self)
		if not VFONT: load_font()
		self.docarea = docarea
		self.app = docarea.app
		self.mw = docarea.app.mw
		self.orient = orient
		self.presenter = docarea.presenter
		self.eventloop = self.presenter.eventloop
		self.doc = self.presenter.model

		self.origin = self.presenter.model.doc_origin
		self.units = self.presenter.model.doc_units
		self.positions = None

		size = config.ruler_size
		if self.orient:
			self.set_size_request(size, -1)
		else:
			self.set_size_request(-1, size)

		self.default_cursor = gtk.gdk.Cursor(gtk.gdk.LEFT_PTR)
		if self.orient == HORIZONTAL:
			self.guide_cursor = self.app.cursors[modes.HGUIDE_MODE]
		else:
			self.guide_cursor = self.app.cursors[modes.VGUIDE_MODE]

		self.set_property(const.PROP_CAN_FOCUS, True)

		self.add_events(gtk.gdk.BUTTON_PRESS_MASK |
					gtk.gdk.POINTER_MOTION_MASK |
					gtk.gdk.BUTTON_RELEASE_MASK)

		self.pointer = []
		self.draw_guide = False

		self.connect(const.EVENT_EXPOSE, self.repaint)
		self.connect(const.EVENT_BUTTON_PRESS, self.mouse_down)
		self.connect(const.EVENT_MOUSE_MOTION, self.mouse_move)
		self.connect(const.EVENT_BUTTON_RELEASE, self.mouse_up)
		self.eventloop.connect(self.eventloop.VIEW_CHANGED, self.repaint)
		self.eventloop.connect(self.eventloop.DOC_MODIFIED, self.check_doc)
		events.connect(events.CONFIG_MODIFIED, self.check_config)

	def close(self):
		events.disconnect(events.CONFIG_MODIFIED, self.check_config)
		fields = self.__dict__
		items = fields.keys()
		for item in items: fields[item] = None

	def check_doc(self, *args):
		origin = self.presenter.model.doc_origin
		units = self.presenter.model.doc_units
		if not self.origin == origin or not self.units == units:
			self.origin = origin
			self.units = units
			self.queue_draw()

	def check_config(self, *args):
		if args[0][0] == 'ruler_size':
			size = config.ruler_size
			if self.orient: self.set_size_request(size, -1)
			else: self.set_size_request(-1, size)
			return
		if args[0][0][:6] == 'ruler_':
			self.queue_draw()

	def update_ruler(self, *args):
		self.queue_draw()

	def calc_ruler(self):
		canvas = self.presenter.canvas
		w, h = self.presenter.get_page_size()
		x = y = 0
		dx = dy = uc2const.unit_dict[self.presenter.model.doc_units]
		origin = self.presenter.model.doc_origin
		if origin == DOC_ORIGIN_LL:
			x0, y0 = canvas.point_doc_to_win([x, y])
		elif origin == DOC_ORIGIN_LU:
			x0, y0 = canvas.point_doc_to_win([x, h + y])
		else:
			x0, y0 = canvas.point_doc_to_win([w / 2.0 + x, h / 2.0 + y])
		dx = dx * canvas.zoom
		dy = dy * canvas.zoom
		sdist = config.snap_distance

		i = 0.0
		while dx < sdist + 3:
			i = i + 0.5
			dx = dx * 10.0 * i
		if dx / 2.0 > sdist + 3:
			dx = dx / 2.0

		i = 0.0
		while dy < sdist + 3:
			i = i + 0.5
			dy = dy * 10.0 * i
		if dy / 2.0 > sdist + 3:
			dy = dy / 2.0

		sx = (x0 / dx - math.floor(x0 / dx)) * dx
		sy = (y0 / dy - math.floor(y0 / dy)) * dy
		return (x0, y0, dx, dy, sx, sy)

	def get_ticks(self):
		canvas = self.presenter.canvas
		pw, ph = self.presenter.get_page_size()
		origin = self.presenter.model.doc_origin
		unit = uc2const.unit_dict[self.presenter.model.doc_units]
		w, h = tuple(self.allocation)[2:]
		x0, y0, dx, dy, sx, sy = self.calc_ruler()
		small_ticks = []
		text_ticks = []

		if self.orient == HORIZONTAL:
			i = -1
			pos = 0
			while pos < w:
				pos = sx + i * dx
				small_ticks.append(sx + i * dx)
				if dx > 10:small_ticks.append(pos + dx * .5)
				i += 1

			coef = round(50.0 / dx)
			if not coef:coef = 1.0
			dxt = dx * coef
			sxt = (x0 / dxt - math.floor(x0 / dxt)) * dxt

			float_flag = False
			unit_dx = dxt / (unit * canvas.zoom)
			if unit_dx < 1.0:float_flag = True

			i = -1
			pos = 0
			shift = 0.0
			if origin == DOC_ORIGIN_CENTER: shift = -pw / 2.0
			while pos < w:
				pos = sxt + i * dxt
				doc_pos = canvas.point_win_to_doc((pos, 0))[0] + shift
				doc_pos *= uc2const.point_dict[self.presenter.model.doc_units]
				if float_flag:
					txt = str(round(doc_pos, 4))
					if not doc_pos:txt = '0'
				else:txt = str(int(round(doc_pos)))
				text_ticks.append((sxt + i * dxt, txt))
				i += 1

		else:
			i = -1
			pos = 0
			while pos < h:
				pos = sy + i * dy
				small_ticks.append(sy + i * dy)
				if dy > 10:small_ticks.append(pos + dy * .5)
				i += 1

			coef = round(50.0 / dy)
			if not coef:coef = 1.0
			dyt = dy * coef
			syt = (y0 / dyt - math.floor(y0 / dyt)) * dyt

			float_flag = False
			unit_dy = dyt / (unit * canvas.zoom)
			if unit_dy < 1.0:float_flag = True

			i = -1
			pos = 0
			shift = 0.0
			if origin == DOC_ORIGIN_CENTER: shift = -ph / 2.0
			if origin == DOC_ORIGIN_LU: shift = -ph
			while pos < h:
				pos = syt + i * dyt
				doc_pos = canvas.point_win_to_doc((0, pos))[1] + shift
				if origin == DOC_ORIGIN_LU:doc_pos *= -1.0
				doc_pos *= uc2const.point_dict[self.presenter.model.doc_units]
				if float_flag:
					txt = str(round(doc_pos, 4))
					if not doc_pos:txt = '0'
				else:txt = str(int(round(doc_pos)))
				text_ticks.append((syt + i * dyt, txt))
				i += 1
		return small_ticks, text_ticks

	def repaint(self, *args):
		if not self.exposed:
#			self.update_colors()
			self.exposed = True
			self.set_cursor(DEFAULT_CURSOR)

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
		self.ctx.set_source_rgb(*CAIRO_WHITE)
		self.ctx.paint()
		self.ctx.set_antialias(cairo.ANTIALIAS_NONE)
		self.ctx.set_line_width(1.0)
		self.ctx.set_dash([])
		self.ctx.set_source_rgba(*CAIRO_BLACK)
		if self.orient == HORIZONTAL:
			self.hrender(w, h)
		else:
			self.vrender(w, h)

		win_ctx.set_source_surface(self.surface)
		win_ctx.paint()

	def hrender(self, w, h):
		self.ctx.move_to(0, h)
		self.ctx.line_to(w, h)

		small_ticks, text_ticks = self.get_ticks()
		for item in small_ticks:
			self.ctx.move_to(item, h - 5)
			self.ctx.line_to(item, h - 1)

		for pos, txt in text_ticks:
			self.ctx.move_to(pos, h - 10)
			self.ctx.line_to(pos, h - 1)

		self.ctx.stroke()

		for pos, txt in text_ticks:
			for character in txt:
				data = HFONT[character]
				self.ctx.set_source_surface(data[1], int(pos), 3)
				self.ctx.paint()
				pos += data[0]

	def vrender(self, w, h):
		self.ctx.move_to(w, 0)
		self.ctx.line_to(w, h)

		small_ticks, text_ticks = self.get_ticks()
		for item in small_ticks:
			self.ctx.move_to(w - 5, item)
			self.ctx.line_to(w - 1, item)

		for item, txt in text_ticks:
			self.ctx.move_to(w - 10, item)
			self.ctx.line_to(w - 1, item)

		self.ctx.stroke()

		for pos, txt in text_ticks:
			for character in txt:
				data = VFONT[character]
				self.ctx.set_source_surface(data[1], 3, int(pos) - data[0])
				self.ctx.paint()
				pos -= data[0]

	#------ Guides creation

	def set_cursor(self, mode=0):
		if mode == DEFAULT_CURSOR:
			self.window.set_cursor(self.default_cursor)
		else:
			self.window.set_cursor(self.guide_cursor)

	def mouse_down(self, widget, event):
		w, h = tuple(self.allocation)[2:]
		w = float(w)
		h = float(h)
		self.width = w
		self.height = h
		self.draw_guide = True
		self.set_cursor()
		self.timer = gobject.timeout_add(RENDERING_DELAY, self.repaint_guide)

	def mouse_up(self, widget, event):
		self.pointer = [event.x, event.y]
		if self.orient == HORIZONTAL:
			y_win = self.pointer[1] - self.height
			if y_win > 0.0:
				p = [self.pointer[0], y_win]
				p, p_doc = self.presenter.snap.snap_point(p, snap_x=False)[1:]
				self.presenter.api.create_guides([[p_doc[1], HORIZONTAL], ])
		else:
			x_win = self.pointer[0] - self.width
			if x_win > 0.0:
				p = [x_win, self.pointer[1]]
				p, p_doc = self.presenter.snap.snap_point(p, snap_y=False)[1:]
				self.presenter.api.create_guides([[p_doc[0], VERTICAL], ])

		self.set_cursor(DEFAULT_CURSOR)
		if not  self.timer is None:
			gobject.source_remove(self.timer)
		self.draw_guide = False
		self.pointer = []
		self.repaint_guide()
		self.canvas.selection_repaint()

	def mouse_move(self, widget, event):
		if self.draw_guide:
			self.pointer = [event.x, event.y]

	def repaint_guide(self, *args):
		p_doc = []
		orient = HORIZONTAL
		if self.draw_guide and self.pointer:
			if self.orient == HORIZONTAL:
				y_win = self.pointer[1] - self.height
				p = [self.pointer[0], y_win]
				p, p_doc = self.presenter.snap.snap_point(p, snap_x=False)[1:]
			else:
				x_win = self.pointer[0] - self.width
				p = [x_win, self.pointer[1]]
				p, p_doc = self.presenter.snap.snap_point(p, snap_y=False)[1:]
				orient = VERTICAL
		self.canvas.renderer.paint_guide_dragging(p_doc, orient)
		return True

	#------ Guides creation end
