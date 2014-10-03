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

def _msg_dialog(parent_win, title, text, secondary_text='', details='',
			dlg_type=gtk.MESSAGE_ERROR):
	dialog = gtk.MessageDialog(parent_win,
					flags=gtk.DIALOG_MODAL,
					type=dlg_type,
					buttons=gtk.BUTTONS_OK,
					message_format=text)
	if secondary_text:
		dialog.format_secondary_text(secondary_text)

	if details:
		expander = gtk.expander_new_with_mnemonic(details[0])

		text_buffer = gtk.TextBuffer()
		text_buffer.set_text(details[1])
		editor = gtk.TextView(text_buffer);
		editor.set_editable(False)
		editor.set_wrap_mode(True)

		sw = gtk.ScrolledWindow()
		sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		sw.add(editor)

		expander.add(sw)
		dialog.vbox.pack_start(expander, True)
		expander.show_all()

	dialog.set_title(title)
	dialog.run()
	dialog.destroy()

def warning_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_WARNING)

def error_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_ERROR)

def info_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_INFO)
