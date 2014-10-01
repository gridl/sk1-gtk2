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

import gtk, rc, gconst

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
