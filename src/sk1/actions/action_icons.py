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
from sk1 import rc, modes
from sk1.actions import action_ids

action_icon = {
modes.SELECT_MODE : wal.IMG_TOOL_SELECT,
modes.SHAPER_MODE : wal.IMG_TOOL_SHAPER,
modes.ZOOM_MODE : wal.IMG_TOOL_ZOOM,
modes.FLEUR_MODE  : wal.IMG_TOOL_FLEUR,
modes.LINE_MODE  : wal.IMG_TOOL_POLYLINE,
modes.CURVE_MODE  : wal.IMG_TOOL_CURVE,
modes.RECT_MODE  : wal.IMG_TOOL_RECT,
modes.ELLIPSE_MODE  : wal.IMG_TOOL_ELLIPSE,
modes.TEXT_MODE  : wal.IMG_TOOL_TEXT,
modes.POLYGON_MODE  : wal.IMG_TOOL_POLYGON,

action_ids.NEW : wal.STOCK_NEW,
action_ids.OPEN : wal.STOCK_OPEN,
action_ids.SAVE : wal.STOCK_SAVE,
action_ids.SAVE_AS : wal.STOCK_SAVE_AS,
action_ids.CLOSE : wal.STOCK_CLOSE,
action_ids.PRINT : wal.STOCK_PRINT,
action_ids.PRINT_SETUP : wal.STOCK_PRINT_PREVIEW,
action_ids.QUIT : wal.STOCK_QUIT,
action_ids.UNDO : wal.STOCK_UNDO,
action_ids.REDO : wal.STOCK_REDO,
action_ids.CUT : wal.STOCK_CUT,
action_ids.CUT2 : wal.STOCK_CUT,
action_ids.CUT3 : wal.STOCK_CUT,
action_ids.COPY : wal.STOCK_COPY,
action_ids.PASTE : wal.STOCK_PASTE,
action_ids.DELETE : wal.STOCK_DELETE,
action_ids.SELECT_ALL : wal.STOCK_SELECT_ALL,
action_ids.ZOOM_IN : wal.STOCK_ZOOM_IN,
action_ids.ZOOM_OUT : wal.STOCK_ZOOM_OUT,
action_ids.ZOOM_PAGE : wal.STOCK_FILE,
action_ids.ZOOM_100 : wal.STOCK_ZOOM_100,
action_ids.ZOOM_SELECTED : wal.STOCK_ZOOM_FIT,
action_ids.FORCE_REDRAW : wal.STOCK_REFRESH,
action_ids.PAGE_FRAME : wal.IMG_CTX_PAGE_FRAME,
action_ids.PAGE_GUIDE_FRAME : wal.IMG_CTX_PAGE_GUIDE_FRAME,
action_ids.REMOVE_ALL_GUIDES : wal.IMG_CTX_REMOVE_ALL_GUIDES,
action_ids.GUIDES_AT_CENTER : wal.IMG_CTX_GUIDES_AT_CENTER,
action_ids.CONVERT_TO_CURVES : wal.IMG_CTX_OBJECT_TO_CURVE,
action_ids.PAGES : rc.STOCK_PLUGIN_PAGES,
action_ids.LAYERS : rc.STOCK_PLUGIN_LAYERS,
action_ids.DOM_VIEWER : rc.STOCK_PLUGIN_DOM_VIEWER,
action_ids.PROPERTIES : wal.STOCK_PROPERTIES,
action_ids.PREFERENCES : wal.STOCK_PREFERENCES,
action_ids.REPORT_BUG : wal.STOCK_DIALOG_WARNING,
action_ids.ABOUT : wal.STOCK_ABOUT,
action_ids.ROTATE_LEFT : wal.IMG_CTX_OBJECT_ROTATE_LEFT,
action_ids.ROTATE_RIGHT : wal.IMG_CTX_OBJECT_ROTATE_RIGHT,
action_ids.VERT_MIRROR : wal.IMG_CTX_VERT_MIRROR,
action_ids.HOR_MIRROR : wal.IMG_CTX_HOR_MIRROR,
action_ids.SNAP_TO_GRID : wal.IMG_CTX_SNAP_TO_GRID,
action_ids.SNAP_TO_GUIDES : wal.IMG_CTX_SNAP_TO_GUIDES,
action_ids.SNAP_TO_OBJECTS : wal.IMG_CTX_SNAP_TO_OBJECTS,
action_ids.SNAP_TO_PAGE : wal.IMG_CTX_SNAP_TO_PAGE,
}

def get_action_icon(action):
	if action in action_icon.keys():
		return action_icon[action]
	else:
		return None
