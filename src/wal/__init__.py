# -*- coding: utf-8 -*-
#
#   Gtk+ 2.0 Widgetset Abstraction Layer
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

from const import *
from image_ids import *

from rc import registry_aliases, registry_provider

from window import MainWindow, MW_Menu, MW_Toolbar
from boxes import HBox, VBox, HidableHBox, HidableVBox, HidableVArea
from widgets import HLine, VLine, Button, ImgButton, ActionButton
from widgets import Label, DecorLabel, Image, ClickableImage, CheckButton
from widgets import ToggleButton, ImgToggleButton, ActionToggleButton
from widgets import ComboBoxText, ComboBoxEntry, ColorButton, RadioButton
from widgets import SpinButton, SpinButtonInt, URL_Label, Entry, TextView
from widgets import NoteBook, Frame, DBTabButton, DBTabLabel, DocBook
from canvas import ColorPlate, ImgPlate, ActiveColorPlate, CairoCanvas

from dialogs import info_dialog, warning_dialog, error_dialog
from dialogs import ask_save_dialog, yesno_dialog, yesnocancel_dialog