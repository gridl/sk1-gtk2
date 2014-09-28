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

from sk1 import _, modes
from sk1.actions import action_ids

action_text = {
modes.SELECT_MODE : _('Selection mode'),
modes.SHAPER_MODE : _('Edit mode'),
modes.ZOOM_MODE : _('Zoom mode'),
modes.FLEUR_MODE : _('Fleur mode'),
modes.LINE_MODE : _('Create polyline'),
modes.CURVE_MODE : _('Create paths'),
modes.RECT_MODE : _('Create rectangle'),
modes.ELLIPSE_MODE : _('Create ellipse'),
modes.TEXT_MODE : _('Create text'),
modes.POLYGON_MODE : _('Create polygon'),
modes.ZOOM_OUT_MODE : _('Zoom out mode'),
modes.MOVE_MODE : _('Move mode'),
modes.COPY_MODE : _('Copy mode'),

action_ids.NEW : _('_New'),
action_ids.OPEN : _('_Open'),
action_ids.IMPORT_IMAGE : _('_Import image'),
action_ids.SAVE : _('_Save'),
action_ids.SAVE_AS : _('Save _As...'),
action_ids.SAVE_ALL : _('Save All'),
action_ids.CLOSE : _('_Close'),
action_ids.CLOSE_ALL : _('_Close All'),
action_ids.PRINT : _('_Print...'),
action_ids.PRINT_SETUP : _('Print Setup...'),
action_ids.QUIT : _('_Exit'),
action_ids.UNDO : _('_Undo'),
action_ids.REDO : _('_Redo'),
action_ids.CLEAR_HISTORY : _('Clear undo history'),
action_ids.CUT : _('Cu_t'),
action_ids.CUT2 : _('Cut'),
action_ids.CUT3 : _('Cut'),
action_ids.COPY : _('_Copy'),
action_ids.PASTE : _('_Paste'),
action_ids.PASTE2 : _('_Paste'),
action_ids.PASTE3 : _('_Paste'),
action_ids.DELETE : _('_Delete'),
action_ids.DELETE2 : _('_Delete'),
action_ids.SELECT_ALL : _('_Select All'),
action_ids.DESELECT : _('_Deselect'),
action_ids.ZOOM_IN : _('Zoom in'),
action_ids.ZOOM_OUT : _('Zoom out'),
action_ids.ZOOM_PAGE : _('Fit zoom to page'),
action_ids.ZOOM_100 : _('Zoom 100%'),
action_ids.ZOOM_SELECTED : _('Zoom selected'),
action_ids.ZOOM_PREVIOUS : _('Previous zoom'),
action_ids.FORCE_REDRAW : _('Redraw document'),
action_ids.PAGE_FRAME : _('Create page frame'),
action_ids.PAGE_GUIDE_FRAME : _('Guides along page border'),
action_ids.REMOVE_ALL_GUIDES : _('Remove all guides'),
action_ids.GUIDES_AT_CENTER : _('Guides at page center'),
action_ids.INSERT_PG : _('Insert page...'),
action_ids.DELETE_PG : _('Delete page...'),
action_ids.GOTO_PG : _('Go to page...'),
action_ids.NEXT_PG : _('Next page'),
action_ids.NEXT_PG_KP : _('Next page'),
action_ids.PREV_PG : _('Previous page'),
action_ids.PREV_PG_KP : _('Previous page'),
action_ids.COMBINE : _('_Combine'),
action_ids.BREAK_APART : _('_Break apart'),
action_ids.GROUP : _('_Group'),
action_ids.UNGROUP : _('_Ungroup'),
action_ids.UNGROUP_ALL : _('U_ngroup all'),
action_ids.CONVERT_TO_CURVES : _('Con_vert to curves'),
action_ids.EDIT_TEXT : _('_Edit text...'),
action_ids.SET_CONTAINER : _('_Place into container'),
action_ids.UNPACK_CONTAINER : _('_Extract from container'),
action_ids.PAGES : _('_Pages'),
action_ids.LAYERS : _('_Layers'),
action_ids.DOM_VIEWER : _('_Object browser'),
action_ids.PROPERTIES : _('Document Properties...'),
action_ids.PREFERENCES : _('Preferences...'),
action_ids.REPORT_BUG : _('_Report bug'),
action_ids.PROJECT_WEBSITE : _('Project _web site'),
action_ids.PROJECT_FORUM : _('Project _forum'),
action_ids.ABOUT : _('_About sK1'),
action_ids.ROTATE_LEFT : _('Rotate _Left'),
action_ids.ROTATE_RIGHT : _('Rotate _Right'),
action_ids.VERT_MIRROR : _('Flip _vertically'),
action_ids.HOR_MIRROR : _('Flip _horizontally'),
action_ids.STROKE_VIEW : _('Stroke View'),
action_ids.DRAFT_VIEW : _('Draft View'),
action_ids.SHOW_GRID : _('Show grid'),
action_ids.SHOW_GUIDES : _('Show guides'),
action_ids.SHOW_SNAP : _('Show active snapping'),
action_ids.SHOW_PAGE : _('Show page border'),
action_ids.SNAP_TO_GRID : _('Snap to grid'),
action_ids.SNAP_TO_GUIDES : _('Snap to guides'),
action_ids.SNAP_TO_OBJECTS : _('Snap to objects'),
action_ids.SNAP_TO_PAGE : _('Snap to page'),
}


def get_action_text(action):
	if action in action_text.keys():
		return action_text[action]
	else:
		return '???'

def get_action_tooltip_text(action):
	return get_action_text(action).replace('_', '')
