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


from sk1.events import CLIPBOARD, DOC_CHANGED, PAGE_CHANGED, \
DOC_CLOSED, DOC_MODIFIED, DOC_SAVED, NO_DOCS, SELECTION_CHANGED
from sk1.widgets import AppAction, AppToggleAction

from action_ids import *
from action_icons import get_action_icon
from action_texts import get_action_text, get_action_tooltip_text
from action_accelkey import get_action_accelkey

def create_actions(app):
	insp = app.inspector
	proxy = app.proxy
	accelgroup = app.accelgroup
	actiongroup = app.actiongroup
	actions = {}
	doc_chnl = [NO_DOCS, DOC_CHANGED]
	docm_chnl = [NO_DOCS, DOC_CHANGED, DOC_MODIFIED]
	page_chnl = docm_chnl + [PAGE_CHANGED]
	sel_chnl = [NO_DOCS, DOC_CHANGED, SELECTION_CHANGED]
	entries = [
#	id, callable, [channels], validator, args
#	name, label, tooltip, icon, shortcut, callable, [channels], validator, args
#gtk.accelerator_name(ord('+'),gtk.gdk.CONTROL_MASK)

[NEW, proxy.new, None, None],
[OPEN, proxy.open, None, None],

	]

	for entry in entries:
		aid = entry[0]
		entry = [aid,
				get_action_text(aid),
				get_action_tooltip_text(aid),
				get_action_icon(aid),
				get_action_accelkey(aid)] + entry[1:]
		if len(entry) == 8:
			action = AppAction(*entry)
		else:
			action = AppToggleAction(*entry)

		actions[entry[0]] = action
		if not action.shortcut is None:
			actiongroup.add_action_with_accel(action, action.shortcut)
			action.set_accel_group(accelgroup)
		else:
			actiongroup.add_action(action)

	return actions