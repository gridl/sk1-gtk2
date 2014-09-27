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

import gtk, gconst, rc, gobject

class HLine(gtk.HSeparator):

	def __init__(self, master):
		self.master = master
		gtk.HSeparator.__init__(self)

class VLine(gtk.VSeparator):

	def __init__(self, master):
		self.master = master
		gtk.VSeparator.__init__(self)

class Button(gtk.Button):

	timer_id = None

	def __init__(self, master, text=None, stock=None, cmd=None, repeat=False):
		self.master = master
		self.cmd = cmd
		gtk.Button.__init__(self, text, stock)
		if cmd: self.connect(gconst.EVENT_CLICKED, cmd)
		if cmd and repeat:
			self.connect(gconst.EVENT_BUTTON_PRESS, self.mouse_pressed)
			self.connect(gconst.EVENT_BUTTON_RELEASE, self.mouse_released)

	def mouse_pressed(self, widget, event):
		if not event.button == gconst.LEFT_BUTTON: return
		self.timer_id = gobject.timeout_add(50, self.do_callback)

	def do_callback(self, *args):
		self.cmd()
		return True

	def mouse_released(self, widget, event):
		if not event.button == gconst.LEFT_BUTTON: return
		if self.timer_id:
			gobject.source_remove(self.timer_id)
			self.timer_id = None

class ImgButton(Button):

	def __init__(self, master, image_id, tooltip='', cmd=None, repeat=False):
		Button.__init__(self, master, cmd=cmd, repeat=repeat)
		self.add(rc.get_image(image_id))
		if tooltip:self.set_tooltip_text(tooltip)

class FImgButton(ImgButton):

	def __init__(self, master, image_id, tooltip='', cmd=None, repeat=False):
		ImgButton.__init__(self, master, image_id, tooltip, cmd, repeat)
		self.set_property('relief', gtk.RELIEF_NONE)
