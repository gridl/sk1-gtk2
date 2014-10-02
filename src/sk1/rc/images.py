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

import os
from sk1 import config

IMG_APP_ICON = 'sk1-app-icon'
IMG_DOC_ICON = 'sk1-document-icon'
IMG_CAIRO_BANNER = 'sk1-cairo-banner'
IMG_SPLASH_TRIADA = 'sk1-splash-triada'

IMG_TOOL_CURVE = 'sk1-tool-curve'
IMG_TOOL_ELLIPSE = 'sk1-tool-ellipse'
IMG_TOOL_FILL = 'sk1-tool-fill'
IMG_TOOL_FLEUR = 'sk1-tool-fleur'
IMG_TOOL_GRADIENT = 'sk1-tool-gradient'
IMG_TOOL_POLYGON = 'sk1-tool-polygon'
IMG_TOOL_POLYLINE = 'sk1-tool-polyline'
IMG_TOOL_RECT = 'sk1-tool-rect'
IMG_TOOL_SELECT = 'sk1-tool-select'
IMG_TOOL_SHAPER = 'sk1-tool-shaper'
IMG_TOOL_STROKE = 'sk1-tool-stroke'
IMG_TOOL_TEXT = 'sk1-tool-text'
IMG_TOOL_ZOOM = 'sk1-tool-zoom'

IMG_RULER_BG = 'sk1-ruler-corner-bg'
IMG_RULER_DO_LL = 'sk1-ruler-docorigin-ll'
IMG_RULER_DO_LU = 'sk1-ruler-docorigin-lu'
IMG_RULER_DO_C = 'sk1-ruler-docorigin-c'

IMG_PAGER_END = 'sk1-pager-end'
IMG_PAGER_NEXT = 'sk1-pager-next'
IMG_PAGER_PREV = 'sk1-pager-prev'
IMG_PAGER_START = 'sk1-pager-start'

IMG_PREFS_CMS = 'sk1-prefs-cms'
IMG_PREFS_CMS_BANNER = 'sk1-prefs-cms-banner'
IMG_PREFS_RULER = 'sk1-prefs-ruler'
IMG_PREFS_PALETTE = 'sk1-prefs-palette'

IMG_CTX_JUMP = 'sk1-ctx-jump'
IMG_CTX_UNITS = 'sk1-ctx-units'
IMG_CTX_LANDSCAPE = 'sk1-ctx-page-landscape'
IMG_CTX_PORTRAIT = 'sk1-ctx-page-portrait'
IMG_CTX_ROTATE = 'sk1-ctx-rotate-selection'
IMG_CTX_GUIDES_AT_CENTER = 'sk1-ctx-guides-at-center'
IMG_CTX_HOR_MIRROR = 'sk1-ctx-hor-mirror'
IMG_CTX_OBJECT_ROTATE_LEFT = 'sk1-ctx-object-rotate-left'
IMG_CTX_OBJECT_ROTATE_RIGHT = 'sk1-ctx-object-rotate-right'
IMG_CTX_OBJECT_TO_CURVE = 'sk1-ctx-object-to-curve'
IMG_CTX_PAGE_FRAME = 'sk1-ctx-page-frame'
IMG_CTX_PAGE_GUIDE_FRAME = 'sk1-ctx-page-guide-frame'
IMG_CTX_REMOVE_ALL_GUIDES = 'sk1-ctx-remove-all-guides'
IMG_CTX_SNAP_TO_GRID = 'sk1-ctx-snap-to-grid'
IMG_CTX_SNAP_TO_GUIDES = 'sk1-ctx-snap-to-guides'
IMG_CTX_SNAP_TO_OBJECTS = 'sk1-ctx-snap-to-objects'
IMG_CTX_SNAP_TO_PAGE = 'sk1-ctx-snap-to-page'
IMG_CTX_VERT_MIRROR = 'sk1-ctx-vert-mirror'
IMG_KEEP_RATIO = 'sk1-ctx-keep-ratio'
IMG_DONT_KEEP_RATIO = 'sk1-ctx-dont-keep-ratio'
IMG_CTX_W_ON_H = 'sk1-ctx-w-on-h'

IMG_PALETTE_ARROW_BOTTOM = 'sk1-palette-arrow-bottom'
IMG_PALETTE_ARROW_LEFT = 'sk1-palette-arrow-left'
IMG_PALETTE_ARROW_RIGHT = 'sk1-palette-arrow-right'
IMG_PALETTE_ARROW_TOP = 'sk1-palette-arrow-top'
IMG_PALETTE_CMYK_COLOR = 'sk1-palette-cmyk_color'
IMG_PALETTE_DOUBLE_ARROW_BOTTOM = 'sk1-palette-double-arrow-bottom'
IMG_PALETTE_DOUBLE_ARROW_LEFT = 'sk1-palette-double-arrow-left'
IMG_PALETTE_DOUBLE_ARROW_RIGHT = 'sk1-palette-double-arrow-right'
IMG_PALETTE_DOUBLE_ARROW_TOP = 'sk1-palette-double-arrow-top'
IMG_PALETTE_NO_COLOR = 'sk1-palette-no-color'
IMG_PALETTE_RGB_COLOR = 'sk1-palette-rgb-color'

def get_image_path(image_id):
	imgdir = os.path.join(config.resource_dir, 'images')
	imgname = image_id + '.png'
	imgpath = os.path.join(imgdir, imgname)
	if os.path.lexists(imgpath): return imgpath
	return None

