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


from gi.repository import Gtk
from sk1 import rc
from sk1.actions.action_ids import *

action_icon = {
NEW : Gtk.STOCK_NEW,
OPEN : Gtk.STOCK_OPEN,
SAVE : Gtk.STOCK_SAVE,
SAVE_AS : Gtk.STOCK_SAVE_AS,
CLOSE : Gtk.STOCK_CLOSE,
PRINT : Gtk.STOCK_PRINT,
PRINT_SETUP : Gtk.STOCK_PRINT_PREVIEW,
QUIT : Gtk.STOCK_QUIT,
UNDO : Gtk.STOCK_UNDO,
REDO : Gtk.STOCK_REDO,
CUT : Gtk.STOCK_CUT,
CUT2 : Gtk.STOCK_CUT,
CUT3 : Gtk.STOCK_CUT,
COPY : Gtk.STOCK_COPY,
PASTE : Gtk.STOCK_PASTE,
DELETE : Gtk.STOCK_DELETE,
SELECT_ALL : Gtk.STOCK_SELECT_ALL,
ZOOM_IN : Gtk.STOCK_ZOOM_IN,
ZOOM_OUT : Gtk.STOCK_ZOOM_OUT,
ZOOM_PAGE : Gtk.STOCK_FILE,
ZOOM_100 : Gtk.STOCK_ZOOM_100,
ZOOM_SELECTED : Gtk.STOCK_ZOOM_FIT,
FORCE_REDRAW : Gtk.STOCK_REFRESH,
PAGE_FRAME : rc.STOCK_PAGE_FRAME,
PAGE_GUIDE_FRAME : rc.STOCK_PAGE_GUIDE_FRAME,
REMOVE_ALL_GUIDES : rc.STOCK_REMOVE_ALL_GUIDES,
GUIDES_AT_CENTER : rc.STOCK_GUIDES_AT_CENTER,
CONVERT_TO_CURVES : rc.STOCK_TO_CURVE,
PAGES : rc.STOCK_PLUGIN_PAGES,
LAYERS : rc.STOCK_PLUGIN_LAYERS,
DOM_VIEWER : rc.STOCK_PLUGIN_DOM_VIEWER,
PROPERTIES : Gtk.STOCK_PROPERTIES,
PREFERENCES : Gtk.STOCK_PREFERENCES,
REPORT_BUG : Gtk.STOCK_DIALOG_WARNING,
ABOUT : Gtk.STOCK_ABOUT,
ROTATE_LEFT : rc.STOCK_ROTATE_LEFT,
ROTATE_RIGHT : rc.STOCK_ROTATE_RIGHT,
VERT_MIRROR : rc.STOCK_VERT_MIRROR,
HOR_MIRROR : rc.STOCK_HOR_MIRROR,
SNAP_TO_GRID : rc.STOCK_SNAP_TO_GRID,
SNAP_TO_GUIDES : rc.STOCK_SNAP_TO_GUIDES,
SNAP_TO_OBJECTS : rc.STOCK_SNAP_TO_OBJECTS,
SNAP_TO_PAGE : rc.STOCK_SNAP_TO_PAGE,
}

def get_action_icon(action):
	if action in action_icon.keys():
		return action_icon[action]
	else:
		return None
