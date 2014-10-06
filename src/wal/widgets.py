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
	def get_text(self):return gtk.Label.get_text(self)
	def set_sensitive(self, val): gtk.Label.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Label.get_sensitive(self)

class DecorLabel(Label):

	text = ''
	markup = ''

	def __init__(self, master, text='', size=0, bold=False,
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
	def set_width(self, width):self.set_size_request(width, -1)

class URL_Label(gtk.EventBox):

	cursor_flag = False

	def __init__(self, master, url, text='', tooltip=''):
		self.url = url
		self.master = master
		gtk.EventBox.__init__(self)
		if tooltip: self.set_tooltip_text(tooltip)
		if not text: text = url
		self.label = Label(self)
		self.label.set_markup('<u>%s</u>' % (text))
		color = rc.rgb_to_gdkcolor(rc.SYSCOLORS['selected-bg'])
		self.label.modify_fg(gtk.STATE_NORMAL, color)
		self.add(self.label)
		self.connect(gconst.EVENT_BUTTON_PRESS, self._mouse_pressed)
		self.connect(gconst.EVENT_ENTER_NOTIFY, self._set_cursor)

	def _mouse_pressed(self, *args):
		import webbrowser
		webbrowser.open_new(self.url)

	def _set_cursor(self, *args):
		if not self.cursor_flag:
			self.cursor_flag = True
			self.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))

class Image(gtk.Image):

	def __init__(self, master, image_id, size=rc.FIXED16):
		self.master = master
		gtk.Image.__init__(self)
		self.set_image(image_id, size)
	def set_sensitive(self, val): gtk.Image.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Image.get_sensitive(self)
	def set_image(self, image_id, size=rc.FIXED16):
		self.set_from_pixbuf(rc.get_pixbuf(image_id, size))

class ActiveImage(gtk.EventBox):

	image = None

	def __init__(self, master, image_id, size=rc.FIXED16, tooltip='', cmd=None):
		self.master = master
		self.cmd = cmd
		gtk.EventBox.__init__(self)
		self.image = Image(self, image_id, size)
		self.add(self.image)
		if tooltip: self.set_tooltip_text(tooltip)
		if cmd: self.connect(gconst.EVENT_BUTTON_PRESS, self._mouse_pressed)

	def _mouse_pressed(self, widget, event):
		if event.button == gconst.LEFT_BUTTON:
			self.cmd(gconst.LEFT_BUTTON)
		if event.button == gconst.RIGHT_BUTTON:
			self.cmd(gconst.RIGHT_BUTTON)
	def set_sensitive(self, val): self.image.set_sensitive(self, val)
	def get_sensitive(self): return self.image.get_sensitive(self)
	def set_tooltip(self, txt):self.set_tooltip_text(txt)
	def set_image(self, image_id, size=rc.FIXED16):
		self.image.set_image(image_id, size)

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

	def set_sensitive(self, val): gtk.Button.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Button.get_sensitive(self)

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
		Button.__init__(self, master)
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

class CheckButton(gtk.CheckButton):

	def __init__(self, master, text, state=False, cmd=None):
		self.master = master
		gtk.CheckButton.__init__(self, text)
		self.set_active(state)
		if cmd: self.connect(gconst.EVENT_TOGGLED, cmd)

	def set_sensitive(self, val): gtk.CheckButton.set_sensitive(self, val)
	def get_sensitive(self): return gtk.CheckButton.get_sensitive(self)
	def set_active(self, val):gtk.CheckButton.set_active(self, val)
	def get_active(self):return gtk.CheckButton.get_active(self)

class RadioButton(gtk.RadioButton):

	def __init__(self, master, text, group=None, state=False, cmd=None):
		self.master = master
		gtk.RadioButton.__init__(self, group, text)
		self.set_active(state)
		if cmd: self.connect(gconst.EVENT_TOGGLED, cmd)

	def set_sensitive(self, val): gtk.RadioButton.set_sensitive(self, val)
	def get_sensitive(self): return gtk.RadioButton.get_sensitive(self)
	def set_active(self, val):gtk.RadioButton.set_active(self, val)
	def get_active(self):return gtk.RadioButton.get_active(self)
	def set_group(self, radiobutton):gtk.RadioButton.set_group(self, radiobutton)
	def get_group(self):return gtk.RadioButton.get_group(self)

class ColorButton(gtk.ColorButton):

	def __init__(self, master, color, title='', cmd=None):
		self.master = master
		gtk.ColorButton.__init__(self)
		self.set_color(color)
		if cmd:self.connect(gconst.EVENT_COLOR_SET, cmd)
		if title:self.set_title(title)

	def set_color(self, color):
		gtk.ColorButton.set_color(self, rc.rgb_to_gdkcolor(color))

	def get_color(self):
		return rc.gdkcolor_to_rgb(gtk.ColorButton.get_color(self))

	def set_sensitive(self, val): gtk.ColorButton.set_sensitive(self, val)
	def get_sensitive(self): return gtk.ColorButton.get_sensitive(self)

class ComboBoxText(gtk.ComboBox):

	def __init__(self, master, listdata=[], cmd=None):
		self.master = master
		self.liststore = gtk.ListStore(gobject.TYPE_STRING)
		gtk.ComboBox.__init__(self, self.liststore)
		cell = gtk.CellRendererText()
		self.pack_start(cell, True)
		self.add_attribute(cell, 'text', 0)
		self.set_list(listdata)
		self.set_active(0)
		if cmd: self.connect(gconst.EVENT_CHANGED, cmd)

	def clear(self):
		self.liststore.clear()

	def set_list(self, datalist=[]):
		if datalist:
			for item in datalist:
				self.append_text(item)

	def get_active(self):return gtk.ComboBox.get_active(self)
	def set_active(self, index):gtk.ComboBox.set_active(self, index)
	def set_sensitive(self, val): gtk.ComboBox.set_sensitive(self, val)
	def get_sensitive(self): return gtk.ComboBox.get_sensitive(self)

class ComboBoxEntry(gtk.ComboBoxEntry):

	callback = None

	def __init__(self, master, listdata=[], editable=False, cmd=None):
		self.master = master
		self.callback = cmd
		self.liststore = gtk.ListStore(gobject.TYPE_STRING)
		gtk.ComboBoxEntry.__init__(self, self.liststore)
		self.set_list(listdata)
		self.set_active(0)
		self.set_editable(editable)
		if cmd: self.child.connect(gconst.EVENT_CHANGED, self._changed)

	def _changed(self, *args): self.callback()

	def set_editable(self, value=True):
		self.child.set_property(gconst.PROP_EDITABLE, value)
		self.child.set_property(gconst.PROP_CAN_FOCUS, value)
		self.set_focus_on_click(value)

	def get_editable(self):
		return self.child.get_property(gconst.PROP_EDITABLE)

	def clear(self):
		self.liststore.clear()

	def set_list(self, datalist=[]):
		maxsize = 1
		if datalist:
			for item in datalist:
				self.append_text(item)
				maxsize = max(len(item), maxsize)
		font_size = rc.SYSFONT['size']
		self.set_size_request(max(maxsize * font_size, 65), 20)

	def get_text(self):
		return self.child.get_text()

	def set_text(self, text):
		self.child.set_text(text)

	def get_active(self):return gtk.ComboBoxEntry.get_active(self)
	def set_active(self, index):gtk.ComboBoxEntry.set_active(self, index)
	def set_sensitive(self, val): gtk.ComboBoxEntry.set_sensitive(self, val)
	def get_sensitive(self): return gtk.ComboBoxEntry.get_sensitive(self)

class SpinButton(gtk.SpinButton):

	change_flag = False
	cmd = None
	check_enter = True

	def __init__(self, master, val=0.0, rng=(0.0, 1.0), incr=0.1, cmd=None,
				check_focus=False, check_enter=True):
		self.master = master
		self.cmd = cmd
		self.check_enter = check_enter
		#value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0
		self.adj = gtk.Adjustment(val, rng[0], rng[1], incr, 1.0, 0.0)
		gtk.SpinButton.__init__(self, self.adj, 0.1, 2)
		self.set_numeric(True)
		font_size = rc.SYSFONT['size']
		self.set_size_request(max(7 * font_size, 65), -1)
		self.connect(gconst.EVENT_VALUE_CHANGED, self._check_changes)
		self.connect(gconst.EVENT_KEY_PRESS, self._check_enter)
		if check_focus:
			self.connect(gconst.EVENT_FOCUS_OUT, self._apply_changes)

	def _check_changes(self, *args):
		self.change_flag = True
		if not self.check_enter: self._apply_changes()

	def _check_enter(self, widget, event):
		keyval = event.keyval
		if keyval in [gconst.KEY_RETURN, gconst.KEY_KP_ENTER]:
			self._apply_changes()
		else: self.change_flag = True

	def _apply_changes(self, *args):
		if self.change_flag:
			self.change_flag = False
			self._do_callback()

	def _do_callback(self):
		if self.cmd: self.cmd()

	def set_value(self, value):
		if not self.check_enter:
			self.check_enter = True
			gtk.SpinButton.set_value(self, value)
			self.check_enter = False
		else:
			gtk.SpinButton.set_value(self, value)
		self.change_flag = False

	def get_value(self):return gtk.SpinButton.get_value(self)

	def set_digits(self, value):
		if not self.check_enter:
			self.check_enter = True
			gtk.SpinButton.set_digits(self, value)
			self.check_enter = False
		else:
			gtk.SpinButton.set_digits(self, value)
		self.change_flag = False

	def set_lower(self, value): self.adj.set_lower(value)
	def set_upper(self, value): self.adj.set_upper(value)
	def set_step_increment(self, value): self.adj.set_step_increment(value)
	def set_page_increment(self, value): self.adj.set_page_increment(value)
	def set_sensitive(self, val): gtk.SpinButton.set_sensitive(self, val)
	def get_sensitive(self): return gtk.SpinButton.get_sensitive(self)
	def set_range(self, rng):
		self.set_lower(rng[0])
		self.set_upper(rng[1])

class SpinButtonInt(SpinButton):

	def __init__(self, master, val=0, rng=(0, 10), incr=1, cmd=None,
				check_focus=False, check_enter=True):
		SpinButton.__init__(self, master, val, rng, incr, cmd,
						check_focus, check_enter)
		SpinButton.set_digits(self, 0)

	def set_value(self, value): SpinButton.set_value(self, int(value))
	def get_value(self): return self.get_value_as_int()
	def set_digits(self, value):pass
	def set_lower(self, value): self.adj.set_lower(int(value))
	def set_upper(self, value): self.adj.set_upper(int(value))
	def set_step_increment(self, value): self.adj.set_step_increment(int(value))
	def set_page_increment(self, value): self.adj.set_page_increment(int(value))

class HScale(gtk.HScale):
	#TODO:class useful for context
	def __init__(self, master):
		gtk.HScale.__init__(self)

class ScaleButton(gtk.ScaleButton):
	#TODO:class useful for plugins
	def __init__(self, master, minval=0, maxval=100, step=2, image_id=''):
		gtk.ScaleButton.__init__(self, gtk.ICON_SIZE_MENU, minval, maxval, step)

class Entry(gtk.Entry):

	change_flag = False
	cmd = None
	check_enter = False

	def __init__(self, master, text='', cmd=None,
				check_focus=False, check_enter=False):
		self.master = master
		self.cmd = cmd
		self.check_enter = check_enter
		gtk.Entry.__init__(self)
		if text:self.set_text(text)
		self.connect(gconst.EVENT_CHANGED, self._check_changes)
		self.connect(gconst.EVENT_KEY_PRESS, self._check_enter)
		if check_focus:
			self.connect(gconst.EVENT_FOCUS_OUT, self._apply_changes)

	def _check_changes(self, *args):
		self.change_flag = True
		if not self.check_enter: self._apply_changes()

	def _check_enter(self, widget, event):
		keyval = event.keyval
		if keyval in [gconst.KEY_RETURN, gconst.KEY_KP_ENTER]:
			self._apply_changes()
		else: self.change_flag = True

	def _apply_changes(self, *args):
		if self.change_flag:
			self.change_flag = False
			self._do_callback()

	def _do_callback(self):
		if self.cmd: self.cmd()

	def set_text(self, text):gtk.Entry.set_text(self, text)
	def get_text(self):return gtk.Entry.get_text(self)
	def set_sensitive(self, val): gtk.Entry.set_sensitive(self, val)
	def get_sensitive(self): return gtk.Entry.get_sensitive(self)
	def set_editable(self, val=True):
		self.set_property(gconst.PROP_EDITABLE, val)

class TextView(gtk.ScrolledWindow):

	def __init__(self, master, text=''):
		self.master = master
		gtk.ScrolledWindow.__init__(self)

		self.text_buffer = gtk.TextBuffer()
		self.text_buffer.set_text(text)
		self.editor = gtk.TextView(self.text_buffer);
		self.editor.set_wrap_mode(gtk.WRAP_WORD)

		self.add(self.editor)
		self.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

	def get_text(self):return self.text_buffer.get_text()
	def set_text(self, text):self.text_buffer.set_text(text)
	def set_sensitive(self, val): self.editor.set_sensitive(val)
	def get_sensitive(self): return self.editor.get_sensitive()
	def set_editable(self, val=True): self.editor.set_editable(val)













