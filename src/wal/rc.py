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

PATH = os.path.dirname(os.path.abspath(__file__))
ICONS_PATH = os.path.join(PATH, 'icons')
GENERIC_ICONS_PATH = os.path.join(ICONS_PATH, 'generic')
ICONS16_PATH = os.path.join(ICONS_PATH, '16x16')
ICONS24_PATH = os.path.join(ICONS_PATH, '24x24')
ICONS32_PATH = os.path.join(ICONS_PATH, '32x32')

FIXED16 = gtk.icon_size_register('FIXED16', 16, 16)
FIXED22 = gtk.icon_size_register('FIXED22', 22, 22)
FIXED24 = gtk.icon_size_register('FIXED24', 24, 24)
FIXED32 = gtk.icon_size_register('FIXED32', 32, 32)

def init_rc():pass

def get_image_path(image_id):
	imgname = image_id + '.png'
	if image_id[:4] == 'sk1-':
		return os.path.join(GENERIC_ICONS_PATH, imgname)
	return None

def get_stock_pixbuf(image_id, size=FIXED16):
	return gtk.Image().render_icon(image_id, size)

def get_pixbuf(image_id, size=FIXED16):
	if image_id[:4] == 'sk1-':
		loader = gtk.gdk.pixbuf_new_from_file
		return loader(get_image_path(image_id))
	else:
		return get_stock_pixbuf(image_id, size)

def get_stock_image(image_id, size=FIXED16):
	image = gtk.Image()
	image.set_from_pixbuf(get_stock_pixbuf(image_id, size))

def get_image(image_id, size=FIXED16):
	if image_id[:4] == 'sk1-':
		image = gtk.Image()
		image.set_from_pixbuf(get_pixbuf(image_id))
		return image
	else:
		return get_stock_image(image_id, size)
	return image
