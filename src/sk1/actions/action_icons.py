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
from sk1.actions.action_ids import *

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

NEW : wal.STOCK_NEW,
OPEN : wal.STOCK_OPEN,
SAVE : wal.STOCK_SAVE,
SAVE_AS : wal.STOCK_SAVE_AS,
CLOSE : wal.STOCK_CLOSE,
PRINT : wal.STOCK_PRINT,
PRINT_SETUP : wal.STOCK_PRINT_PREVIEW,
QUIT : wal.STOCK_QUIT,
UNDO : wal.STOCK_UNDO,
REDO : wal.STOCK_REDO,
CUT : wal.STOCK_CUT,
CUT2 : wal.STOCK_CUT,
CUT3 : wal.STOCK_CUT,
COPY : wal.STOCK_COPY,
PASTE : wal.STOCK_PASTE,
DELETE : wal.STOCK_DELETE,
SELECT_ALL : wal.STOCK_SELECT_ALL,
ZOOM_IN : wal.STOCK_ZOOM_IN,
ZOOM_OUT : wal.STOCK_ZOOM_OUT,
ZOOM_PAGE : wal.STOCK_FILE,
ZOOM_100 : wal.STOCK_ZOOM_100,
ZOOM_SELECTED : wal.STOCK_ZOOM_FIT,
FORCE_REDRAW : wal.STOCK_REFRESH,
PAGE_FRAME : wal.IMG_CTX_PAGE_FRAME,
PAGE_GUIDE_FRAME : wal.IMG_CTX_PAGE_GUIDE_FRAME,
REMOVE_ALL_GUIDES : wal.IMG_CTX_REMOVE_ALL_GUIDES,
GUIDES_AT_CENTER : wal.IMG_CTX_GUIDES_AT_CENTER,
CONVERT_TO_CURVES : wal.IMG_CTX_OBJECT_TO_CURVE,
PAGES : rc.STOCK_PLUGIN_PAGES,
LAYERS : rc.STOCK_PLUGIN_LAYERS,
DOM_VIEWER : rc.STOCK_PLUGIN_DOM_VIEWER,
PROPERTIES : wal.STOCK_PROPERTIES,
PREFERENCES : wal.STOCK_PREFERENCES,
REPORT_BUG : wal.STOCK_DIALOG_WARNING,
ABOUT : wal.STOCK_ABOUT,
ROTATE_LEFT : wal.IMG_CTX_OBJECT_ROTATE_LEFT,
ROTATE_RIGHT : wal.IMG_CTX_OBJECT_ROTATE_RIGHT,
VERT_MIRROR : wal.IMG_CTX_VERT_MIRROR,
HOR_MIRROR : wal.IMG_CTX_HOR_MIRROR,
SNAP_TO_GRID : wal.IMG_CTX_SNAP_TO_GRID,
SNAP_TO_GUIDES : wal.IMG_CTX_SNAP_TO_GUIDES,
SNAP_TO_OBJECTS : wal.IMG_CTX_SNAP_TO_OBJECTS,
SNAP_TO_PAGE : wal.IMG_CTX_SNAP_TO_PAGE,
}

def get_action_icon(action):
	if action in action_icon.keys():
		return action_icon[action]
	else:
		return None
