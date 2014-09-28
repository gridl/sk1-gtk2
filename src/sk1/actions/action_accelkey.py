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


from sk1.actions import action_ids

accelkeys = {
action_ids.NEW : '<Control>N',
action_ids.OPEN : '<Control>O',
action_ids.SAVE : '<Control>S',
action_ids.CLOSE : '<Control>W',
action_ids.PRINT : '<Control>P',
action_ids.QUIT : '<Alt>F4',
action_ids.UNDO : '<Control>Z',
action_ids.REDO : '<Control><Shift>Z',
action_ids.CUT : '<Control>X',
action_ids.CUT2 : '<Shift>Delete',
action_ids.CUT3 : '<Shift>KP_Decimal',
action_ids.COPY : '<Control>C',
action_ids.PASTE : '<Control>V',
action_ids.PASTE2 : '<Shift>Insert',
action_ids.PASTE3 : '<Shift>KP_0',
action_ids.DELETE : 'Delete',
action_ids.DELETE2 : 'KP_Delete',
action_ids.SELECT_ALL : '<Control>A',
action_ids.DESELECT : '<Control><Shift>A',
action_ids.ZOOM_IN : '<Control>equal',
action_ids.ZOOM_OUT : '<Control>minus',
action_ids.ZOOM_PAGE : '<Shift>F4',
action_ids.ZOOM_SELECTED : 'F4',
action_ids.ZOOM_PREVIOUS : 'F3',
action_ids.FORCE_REDRAW : '<Alt>R',
action_ids.NEXT_PG : 'Page_Down',
action_ids.NEXT_PG_KP : 'KP_Page_Down',
action_ids.PREV_PG : 'Page_Up',
action_ids.PREV_PG_KP : 'KP_Page_Up',
action_ids.COMBINE : '<Control>L',
action_ids.BREAK_APART : '<Control>K',
action_ids.GROUP : '<Control>G',
action_ids.UNGROUP : '<Control>U',
action_ids.CONVERT_TO_CURVES : '<Control>Q',
action_ids.EDIT_TEXT : 'F8',
action_ids.PAGES : '<Control>F7',
action_ids.LAYERS : 'F7',
action_ids.STROKE_VIEW : '<Shift>F9',
action_ids.SNAP_TO_GRID : '<Control>Y',
action_ids.SNAP_TO_GUIDES : '<Control>I',
}

def get_action_accelkey(action):
	if action in accelkeys.keys():
		return accelkeys[action]
	else:
		return None
