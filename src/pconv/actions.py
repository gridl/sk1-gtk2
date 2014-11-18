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

import wal
from pconv import _

NEW = 101
OPEN = 102

action_text = {
NEW: _('New'),
OPEN: _('Open'),
}

action_icon = {
NEW : wal.STOCK_NEW,
OPEN: wal.STOCK_OPEN,
}

action_accelkey = {
NEW : '<Control>N',
OPEN : '<Control>O',
}

def get_action_text(action):
	if action in action_text.keys():
		return action_text[action]
	else:
		return '???'

def get_action_tooltip_text(action):
	return get_action_text(action).replace('_', '')


def get_action_icon(action):
	if action in action_icon.keys():
		return action_icon[action]
	else:
		return None

def get_action_accelkey(action):
	if action in action_accelkey.keys():
		return action_accelkey[action]
	else:
		return None

def create_actions(app):
	insp = app.insp
	proxy = app.proxy
	actions = []

	entries = [
[NEW, proxy.new, None, None],
[OPEN, proxy.open, None, None],
	]

	for entry in entries:
		actions.append([entry[0],
				get_action_text(entry[0]),
				get_action_tooltip_text(entry[0]),
				get_action_icon(entry[0]),
				get_action_accelkey(entry[0])] + entry[1:])
	return actions
