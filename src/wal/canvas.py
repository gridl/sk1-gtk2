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

import gtk, rc, gconst, cairo

class ColorPlate(gtk.DrawingArea):

	def __init__(self, master, size=(), bg=()):
		self.master = master
		gtk.DrawingArea.__init__(self)
		if size: self.set_size(*size)
		if bg: self.set_bgcolor(bg)

	def set_size(self, w, h): self.set_size_request(w, h)
	def get_size(self): return tuple(self.allocation)[2:]
	def set_bgcolor(self, color):
		self.modify_bg(gtk.STATE_NORMAL, rc.rgb_to_gdkcolor(color))
	def get_bgcolor(self):
		return rc.gdkcolor_to_rgb(self.get_style().bg[gtk.STATE_NORMAL])

class ImgPlate(ColorPlate):

	image = None

	def __init__(self, master, image_id=None, image_size=rc.FIXED16,
				 size=(), bg=()):
		ColorPlate.__init__(self, master, size, bg)
		self.connect(gconst.EVENT_EXPOSE, self._repaint)
		if image_id:
			self.image = self.load_image(image_id, image_size)
			self.set_size(*self.get_image_size(self.image))

	def repaint_request(self, *args):
		self.queue_draw()

	def load_image(self, image_id, image_size=rc.FIXED16):
		return rc.get_pixbuf(image_id, image_size)

	def get_image_size(self, image):
		return image.get_width(), image.get_height()

	def set_image(self, image_id):
		if image_id:
			self.image = self.load_image(image_id)
			self.repaint_request()

	def draw_image(self, image, x, y):
		frame = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8,
            image.get_width(),
            image.get_height())

		frame.fill(rc.rgb_to_gdkpixel(self.get_bgcolor()))
		image.composite(
			frame,
			0, 0,
            image.get_width(),
            image.get_height(),
            0, 0, 1, 1, gtk.gdk.INTERP_NEAREST, 255)

		self.window.draw_rgb_image(
            self.style.black_gc,
            x, y,
            frame.get_width(),
            frame.get_height(),
            gtk.gdk.RGB_DITHER_NORMAL,
            frame.get_pixels(),
            frame.get_rowstride())

	def draw_image_at_center(self, image):
		width, height = self.get_size()
		x = (width - image.get_width()) / 2
		y = (height - image.get_height()) / 2
		self.draw_image(image, x, y)

	def _repaint(self, *args):
		self.repaint()
		return True

	#--- Stub for subclass repaint method
	def repaint(self):
		if self.image: self.draw_image_at_center(self.image)


class Event:
	pos = ()
	alt = False; ctrl = False; shift = False
	direction = 1
	def __init__(self):pass

class ActiveColorPlate(ColorPlate):

	def __init__(self, master, size=(), bg=()):
		ColorPlate.__init__(self, master, size, bg)
		self.add_events(gtk.gdk.BUTTON_PRESS_MASK |
					gtk.gdk.POINTER_MOTION_MASK |
					gtk.gdk.BUTTON_RELEASE_MASK |
              		gtk.gdk.SCROLL_MASK |
              		gtk.gdk.ENTER_NOTIFY_MASK |
              		gtk.gdk.LEAVE_NOTIFY_MASK)

		self.connect(gconst.EVENT_BUTTON_PRESS, self._press_event)
		self.connect(gconst.EVENT_BUTTON_RELEASE, self._release_event)
		self.connect(gconst.EVENT_MOUSE_MOTION, self._move_event)
		self.connect(gconst.EVENT_MOUSE_SCROLL, self._wheel_event)
		self.connect(gconst.EVENT_ENTER_NOTIFY, self._enter_event)
		self.connect(gconst.EVENT_LEAVE_NOTIFY, self._leave_event)

	def get_event(self, gevent):
		event = Event()
		event.pos = (gevent.x, gevent.y)
		if gevent.type == gtk.gdk.SCROLL and  \
		gevent.direction == gtk.gdk.SCROLL_DOWN: event.direction = -1
		if gevent.state & gtk.gdk.CONTROL_MASK:event.ctrl = True
		if gevent.state & gtk.gdk.SHIFT_MASK:event.shift = True
		if gevent.state & gtk.gdk.MOD1_MASK:event.alt = True
		return event

	def _press_event(self, widget, gevent):
		event = self.get_event(gevent)
		dblclk = False
		if gevent.type == gtk.gdk._2BUTTON_PRESS: dblclk = True
		if gevent.button == gconst.LEFT_BUTTON and dblclk:
			self.mouse_left_dclick(event)
		elif gevent.button == gconst.LEFT_BUTTON and not dblclk:
			self.mouse_left_down(event)
		elif gevent.button == gconst.RIGHT_BUTTON:
			self.mouse_right_down(event)
		elif gevent.button == gconst.MIDDLE_BUTTON:
			self.mouse_middle_down(event)
		return True

	def _release_event(self, widget, gevent):
		event = self.get_event(gevent)
		if gevent.button == gconst.LEFT_BUTTON:
			self.mouse_left_up(event)
		elif gevent.button == gconst.RIGHT_BUTTON:
			self.mouse_right_up(event)
		elif gevent.button == gconst.MIDDLE_BUTTON:
			self.mouse_middle_up(event)
		return True

	def _move_event(self, widget, gevent):
		self.mouse_move(self.get_event(gevent))

	def _wheel_event(self, widget, gevent):
		self.mouse_wheel(self.get_event(gevent))
		return True

	def _enter_event(self, widget, gevent):
		self.mouse_enter(self.get_event(gevent))
		return True

	def _leave_event(self, widget, gevent):
		self.mouse_leave(self.get_event(gevent))
		return True

	#---Stubs for subclass connecting
	def mouse_enter(self, event):pass
	def mouse_leave(self, event):pass
	def mouse_left_down(self, event):pass
	def mouse_left_up(self, event):pass
	def mouse_left_dclick(self, event):pass
	def mouse_right_down(self, event):pass
	def mouse_right_up(self, event):pass
	def mouse_middle_down(self, event):pass
	def mouse_middle_up(self, event):pass
	def mouse_move(self, event):pass
	def mouse_wheel(self, event):pass

class CairoCanvas(ActiveColorPlate):

	ctx = None

	def __init__(self, master, size=(), bg=(), has_tooltip=False):
		ActiveColorPlate.__init__(self, master, size, bg)
		self.connect(gconst.EVENT_EXPOSE, self._repaint)
		if has_tooltip:
			self.set_property(gconst.PROP_HAS_TOOLTIP, True)
			self.connect(gconst.EVENT_QUERY_TOOLTIP, self._update_tooltip)

	def repaint_request(self, *args): self.queue_draw()

	def _update_tooltip(self, *args):
		x = args[1]
		y = args[2]
		tooltip = args[4]
		ret = self.update_tooltip(x, y)
		if not ret or not len(ret) == 3:return False
		if ret[0]: tooltip.set_icon(rc.get_pixbuf(ret[0]))
		markup = ''
		if ret[1]:markup += '<b>%s</b>' % (ret[1])
		if ret[1] and ret[2]:markup += '\n'
		if ret[2]:markup += ret[2]
		if markup: tooltip.set_markup(markup)
		elif not ret[0]:return False
		return True

	#---Stub for subclassing
	def update_tooltip(self, x, y):return ()

	def _repaint(self, *args):
		self.ctx = self.window.cairo_create()
		self.repaint()
		self.ctx = None
		return True

	#---Stub for subclassing
	def repaint(self):pass

	def set_antialias(self, val=True):
		if not self.ctx:return
		if val: self.ctx.set_antialias(cairo.ANTIALIAS_DEFAULT)
		else: self.ctx.set_antialias(cairo.ANTIALIAS_NONE)

	def clear(self):
		if not self.ctx:return
		self.ctx.set_source_rgb(*self.get_bgcolor())
		self.ctx.paint()

	def draw_rect(self, rect):
		"rect - tuple of (x,y,w,h)"
		if not self.ctx:return
		self.ctx.rectangle(*rect)

	def draw_line(self, points):
		"points - sequence of points [(x,y),(x,y)...]"
		if not self.ctx:return
		self.ctx.move_to(*points[0])
		for point in points[1:]:
			self.ctx.line_to(*point)

	def fill(self, color):
		"color- tuple of (r,g,b)"
		if not self.ctx:return
		self.ctx.set_source_rgb(*color)
		self.ctx.fill()

	def stroke(self, color, width=1.0, dashes=()):
		"color- tuple of (r,g,b)"
		if not self.ctx:return
		self.ctx.set_line_width(width)
		self.ctx.set_dash(dashes)
		self.ctx.set_source_rgb(*color)
		self.ctx.stroke()

	def rectangle(self, rect, fill_color, stroke_color, width=1.0, dashes=()):
		"rect - tuple of (x,y,w,h); color- tuple of (r,g,b)"
		if not self.ctx:return
		self.draw_rect(rect)
		self.fill(fill_color)
		self.draw_rect(rect)
		self.stroke(stroke_color, width, dashes)

	def polyline(self, points, stroke_color, width=1.0, dashes=()):
		if not self.ctx:return
		self.draw_line(points)
		self.stroke(stroke_color, width, dashes)
