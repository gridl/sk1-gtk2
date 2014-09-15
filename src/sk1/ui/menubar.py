# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2012 by Igor E. Novikov
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

from sk1 import _, actions

class AppMenubar(gtk.MenuBar):

	def __init__(self, mw):
		gtk.MenuBar.__init__(self)
		self.mw = mw
		self.app = mw.app
		self.actions = self.app.actions

		#----FILE MENU
		self.file_item, self.file_menu = self.create_menu(_("_File"))
		items = [actions.NEW,
				 None,
				 actions.OPEN,
				 actions.SAVE,
				 actions.SAVE_AS,
				 actions.SAVE_ALL,
				 None,
				 actions.CLOSE,
				 actions.CLOSE_ALL,
				 None,
				 actions.IMPORT_IMAGE,
				 None,
				 actions.PRINT_SETUP,
				 actions.PRINT,
				 None,
				 actions.QUIT,
		]
		self.add_items(self.file_menu, items)

		#----EDIT MENU
		self.edit_item, self.edit_menu = self.create_menu(_("_Edit"))
		items = [actions.UNDO,
				 actions.REDO,
				 actions.CLEAR_HISTORY,
				 None,
				 actions.CUT,
				 actions.COPY,
				 actions.PASTE,
				 actions.DELETE,
				 None,
				 actions.SELECT_ALL,
				 actions.DESELECT,
				 None,
				 actions.PROPERTIES,
				 actions.PREFERENCES,
		]
		self.add_items(self.edit_menu, items)

		#----SHOW TO Submenu
		self.show_item, self.show_menu = self.create_menu(_("_Show"))
		items = [actions.SHOW_GRID,
				 actions.SHOW_GUIDES,
				 actions.SHOW_SNAP,
				 actions.SHOW_PAGE, ]
		self.add_items(self.show_menu, items)

		#----SNAP TO Submenu
		self.snap_to_item, self.snap_to_menu = self.create_menu(_("_Snap to"))
		items = [actions.SNAP_TO_GRID,
				 actions.SNAP_TO_GUIDES,
				 actions.SNAP_TO_OBJECTS,
				 actions.SNAP_TO_PAGE, ]
		self.add_items(self.snap_to_menu, items)

		#----VIEW MENU
		self.view_item, self.view_menu = self.create_menu(_("_View"))
		items = [actions.STROKE_VIEW,
				actions.DRAFT_VIEW,
				 None,
				 actions.ZOOM_100,
				 actions.ZOOM_IN,
				 actions.ZOOM_OUT,
				 actions.ZOOM_PREVIOUS,
				 None,
				 actions.ZOOM_PAGE,
				 actions.ZOOM_SELECTED,
				 None,
				 self.show_item,
				 None,
				 self.snap_to_item,
				 None,
				 actions.FORCE_REDRAW,
		]
		self.add_items(self.view_menu, items)

		#----LAYOUT MENU
		self.layout_item, self.layout_menu = self.create_menu(_("_Layout"))
		items = [actions.INSERT_PG,
				 actions.DELETE_PG,
				 actions.GOTO_PG,
				 None,
				 actions.NEXT_PG,
				 actions.PREV_PG,
		]
		self.add_items(self.layout_menu, items)

		#----ARRANGE MENU
		self.arrange_item, self.arrange_menu = self.create_menu(_("_Arrange"))
		items = [actions.COMBINE,
				actions.BREAK_APART,
				None,
				actions.GROUP,
				actions.UNGROUP,
				actions.UNGROUP_ALL,
				None,
				actions.CONVERT_TO_CURVES,
		]
		self.add_items(self.arrange_menu, items)

		#----EFFETCS MENU
		self.effects_item, self.effects_menu = self.create_menu(_("Effe_cts"))
		items = [actions.SET_CONTAINER,
				actions.UNPACK_CONTAINER,
		]
		self.add_items(self.effects_menu, items)

		#----BITMAPS MENU
		self.bitmaps_item, self.curve_menu = self.create_menu(_("_Bitmaps"))

		#----TEXT MENU
		self.text_item, self.text_menu = self.create_menu(_("_Text"))
		items = [actions.EDIT_TEXT,
		]
		self.add_items(self.text_menu, items)

		#----TOOLS MENU
		self.tools_item, self.tools_menu = self.create_menu(_("T_ools"))
		items = [actions.PAGES,
				actions.LAYERS,
				actions.DOM_VIEWER,
		]
		self.add_items(self.tools_menu, items)

		#----HELP MENU
		self.help_item, self.help_menu = self.create_menu(_("_Help"))
		items = [actions.REPORT_BUG,
				None,
				actions.PROJECT_WEBSITE,
				actions.PROJECT_FORUM,
				None,
				actions.ABOUT,
		]
		self.add_items(self.help_menu, items)

		#----HIDDEN MENU
		self.hidden_item, self.hidden_menu = self.create_menu("hidden")
		items = [actions.PREV_PG_KP,
				actions.NEXT_PG_KP,
				actions.CUT2,
				actions.CUT3,
				actions.PASTE2,
				actions.PASTE3,
				actions.DELETE2,
		]
		self.add_items(self.hidden_menu, items)

		self.append(self.file_item)
		self.append(self.edit_item)
		self.append(self.view_item)
		self.append(self.layout_item)
		self.append(self.arrange_item)
		self.append(self.effects_item)
		self.append(self.bitmaps_item)
		self.append(self.text_item)
		self.append(self.tools_item)
		self.append(self.help_item)
#		self.append(self.hidden_item)

	def create_menu(self, text):
		menu = gtk.Menu()
		item = gtk.MenuItem(text)
		item.set_submenu(menu)
		return item, menu

	def add_items(self, parent, items):
		for item in items:
			if item is None:
				parent.append(gtk.SeparatorMenuItem())
			elif isinstance(item, str):
				action = self.actions[item]
				menuitem = action.create_menu_item()
				action.menuitem = menuitem
				parent.append(menuitem)
			else:
				parent.append(item)
