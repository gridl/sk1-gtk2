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

class Label(gtk.Label):

	def __init__(self, master, text=''):
		self.master = master
		gtk.Label.__init__(self, text)

	def set_text(self, text):gtk.Label.set_text(self, text)
	def get_text(self, text):return gtk.Label.get_text(self)
	def set_sensitive(self, val): gtk.Label.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Label.get_sensitive(self)

class DecorLabel(Label):

	text = ''
	markup = ''

	def __init__(self, master, text='', size='', bold=False,
				italic=False, enabled=True, wrap=False):
		self.text = text
		Label.__init__(self, master)
		markup = '%s'
		if italic:markup = '<i>%s</i>' % (markup)
		if bold:markup = '<b>%s</b>' % (markup)
		if size:
			if size == -1:size = 'smaller'
			else:size = 'larger'
			markup = '<span size="%s">%s</span>' % (size, markup)
		self.markup = markup
		self.set_markup(markup % (text))
		if not enabled: self.set_sensitive(False)
		if wrap: self.set_line_wrap(True)

	def set_text(self, text):
		self.text = text
		self.set_markup(self.markup % (text))

	def get_text(self): return self.text

class Image(gtk.Image):
	def __init__(self, master, image_id, size=rc.FIXED16):
		self.master = master
		gtk.Image.__init__(self)
		self.set_from_pixbuf(rc.get_pixbuf(image_id, size))

class ActiveImage(gtk.EventBox):

	def __init__(self, master, image_id, size=rc.FIXED16, tooltip='', cmd=None):
		self.master = master
		self.cmd = cmd
		gtk.EventBox.__init__(self)
		self.add(Image(self, image_id, size))
		if tooltip: self.set_tooltip_text(tooltip)
		if cmd: self.connect('button-press-event', self._mouse_pressed)

	def _mouse_pressed(self, widget, event):
		if event.button == gconst.LEFT_BUTTON:self.cmd(gconst.LEFT_BUTTON)
		if event.button == gconst.RIGHT_BUTTON:self.cmd(gconst.RIGHT_BUTTON)

class Button(gtk.Button):

	timer_id = None

	def __init__(self, master, text=None, stock=None, cmd=None,
				repeat=False, flat=False):
		self.master = master
		self.cmd = cmd
		gtk.Button.__init__(self, text, stock)
		if cmd: self.connect(gconst.EVENT_CLICKED, cmd)
		if cmd and repeat:
			self.connect(gconst.EVENT_BUTTON_PRESS, self._mouse_pressed)
			self.connect(gconst.EVENT_BUTTON_RELEASE, self._mouse_released)
		if flat:self.set_property(gconst.PROP_RELIEF, gtk.RELIEF_NONE)

	def set_sensitive(self, val): gtk.Button.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Button.get_sensitive(self)

	def _mouse_pressed(self, widget, event):
		if not event.button == gconst.LEFT_BUTTON: return
		if not self.timer_id:
			self.timer_id = gobject.timeout_add(50, self._do_callback)

	def _do_callback(self, *args):
		self.cmd()
		return True

	def _mouse_released(self, widget, event):
		if not event.button == gconst.LEFT_BUTTON: return
		if self.timer_id:
			gobject.source_remove(self.timer_id)
			self.timer_id = None

class ImgButton(Button):

	def __init__(self, master, image_id, image_size=rc.FIXED16, tooltip='',
				cmd=None, repeat=False, flat=False):
		Button.__init__(self, master, cmd=cmd, repeat=repeat, flat=flat)
		self.add(rc.get_image(image_id, image_size))
		if tooltip:self.set_tooltip_text(tooltip)

class ToggleButton(gtk.ToggleButton):

	def __init__(self, master, text=None, cmd=None, flat=True):
		self.master = master
		gtk.ToggleButton.__init__(self, text)
		if cmd: self.connect(gconst.EVENT_TOGGLED, cmd)
		if flat:self.set_property(gconst.PROP_RELIEF, gtk.RELIEF_NONE)

	def set_sensitive(self, val): gtk.ToggleButton.set_sensitive(self, val)
	def get_sensitive(self): return gtk.ToggleButton.get_sensitive(self)
	def set_active(self, val):gtk.ToggleButton.set_active(self, val)
	def get_active(self):return gtk.ToggleButton.get_active(self)

class ImgToggleButton(ToggleButton):

	def __init__(self, master, image_id, image_size=rc.FIXED16,
				tooltip='', cmd=None, flat=True):
		ToggleButton.__init__(self, master, cmd=cmd, flat=flat)
		self.add(rc.get_image(image_id, image_size))
		if tooltip:self.set_tooltip_text(tooltip)

class ActionButton(Button):
	def __init__(self, master, action, image_size=rc.FIXED16, flat=True):
		Button.__init__(self)
		if action.icon:
			self.add(rc.get_image(action.icon, image_size))
		self.set_tooltip_text(action.tooltip)
		if flat:self.set_property(gconst.PROP_RELIEF, gtk.RELIEF_NONE)
		action.connect_proxy(self)

class ActionToggleButton(ToggleButton):
	def __init__(self, master, action, image_size=rc.FIXED16, flat=True):
		ToggleButton.__init__(self, master)
		if action.icon:
			self.add(rc.get_image(action.icon, image_size))
		self.set_tooltip_text(action.tooltip)
		if flat:self.set_property(gconst.PROP_RELIEF, gtk.RELIEF_NONE)
		action.connect_proxy(self)
