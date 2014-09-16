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

import os, gtk
from sk1 import config

IMG_APP_ICON = 'sk1-app-icon'
IMG_CAIRO_BANNER = 'sk1-cairo-banner'
IMG_PREFS_CMS = 'sk1-prefs-cms'
IMG_PREFS_CMS_BANNER = 'sk1-prefs-cms-banner'

IMG_CONTEXT_JUMP = 'sk1-context-jump'
IMG_CONTEXT_LANDSCAPE = 'sk1-context-page-landscape'
IMG_CONTEXT_PORTRAIT = 'sk1-context-page-portrait'

def get_image_path(image_id):
	imgdir = os.path.join(config.resource_dir, 'images')
	imgname = image_id + '.png'
	return os.path.join(imgdir, imgname)

def get_pixbuf(image_id):
	loader = gtk.gdk.pixbuf_new_from_file
	return loader(get_image_path(image_id))

def get_stock_pixbuf(image_id, size):
	return gtk.Image().render_icon(image_id, size)

def get_image(image_id):
	image = gtk.Image()
	image.set_from_pixbuf(get_pixbuf(image_id))
	return image

def get_stock_image(image_id, size):
	image = gtk.Image()
	image.set_from_pixbuf(get_stock_pixbuf(image_id, size))
	return image
