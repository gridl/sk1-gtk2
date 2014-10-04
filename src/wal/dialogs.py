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

import gtk, rc, const

RESPONCE = {
		gtk.RESPONSE_OK:const.RESPONSE_OK,
		gtk.RESPONSE_YES:const.RESPONSE_YES,
		gtk.RESPONSE_NO:const.RESPONSE_NO,
		gtk.RESPONSE_CANCEL:const.RESPONSE_CANCEL,
		gtk.RESPONSE_NONE:const.RESPONSE_CANCEL,
		gtk.RESPONSE_DELETE_EVENT:const.RESPONSE_CANCEL,
		}

def _msg_dialog(parent_win, title, text, secondary_text='', details='',
		dlg_type=gtk.MESSAGE_ERROR, buttons=[(gtk.STOCK_OK, gtk.RESPONSE_OK)]):
	dialog = gtk.MessageDialog(parent_win,
					flags=gtk.DIALOG_MODAL,
					type=dlg_type,
					message_format=text)
	dialog.set_title(title)

	for button in buttons:
		dialog.add_button(button[0], button[1])
	dialog.set_default_response(buttons[-1][1])

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
	ret = dialog.run()
	dialog.destroy()
	return ret

def warning_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_WARNING)

def error_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_ERROR)

def info_dialog(parent_win, title, text, secondary_text='', details=()):
	_msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_INFO)

def yesno_dialog(parent_win, title, text, secondary_text='', details=()):
	buttons = [(gtk.STOCK_NO, gtk.RESPONSE_NO),
			(gtk.STOCK_YES , gtk.RESPONSE_YES,)]
	ret = _msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_INFO, buttons)
	return RESPONCE[ret]

def yesnocancel_dialog(parent_win, title, text, secondary_text='', details=()):
	buttons = [(gtk.STOCK_NO, gtk.RESPONSE_NO),
			(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL),
			(gtk.STOCK_YES , gtk.RESPONSE_YES,)]
	ret = _msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_INFO, buttons)
	return RESPONCE[ret]

def ask_save_dialog(parent_win, title, text, secondary_text='', details=()):
	buttons = [(rc.STOCK_DONT_SAVE , gtk.RESPONSE_NO,),
				(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL),
				(gtk.STOCK_SAVE, gtk.RESPONSE_OK)]
	ret = _msg_dialog(parent_win, title, text, secondary_text,
			details, gtk.MESSAGE_WARNING, buttons)
	return RESPONCE[ret]

