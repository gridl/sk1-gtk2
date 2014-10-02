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
FIXED48 = gtk.icon_size_register('FIXED48', 48, 48)
FIXED64 = gtk.icon_size_register('FIXED64', 64, 64)
FIXED128 = gtk.icon_size_register('FIXED128', 128, 128)

STOCK_ZOOM_PAGE = 'gtk-zoom-page'
STOCK_DONT_SAVE = 'gtk-action-dont-save'

def init_rc():pass

def registry_aliases(aliases):

	iconfactory = gtk.IconFactory()
	gtk.stock_add([(STOCK_ZOOM_PAGE, '', 0, 0, ''), ])

	items = [gtk.STOCK_ZOOM_100, gtk.STOCK_ZOOM_FIT, gtk.STOCK_ZOOM_IN,
			gtk.STOCK_ZOOM_OUT, STOCK_ZOOM_PAGE]

	for item in items:
		iconset = gtk.IconSet()
		source = gtk.IconSource()
		filepath = os.path.join(ICONS24_PATH, item + '.png')
		pixbuf = gtk.gdk.pixbuf_new_from_file(filepath)
		source.set_pixbuf(pixbuf)
		source.set_size_wildcarded(True)
		iconset.add_source(source)
		iconfactory.add(item, iconset)

	if aliases:
		items = []
		alias_items = []
		for item in aliases:
			items.append(item[0])
			alias_items.append(item[1])

		gtk.stock_add(items)

		for item, alias in alias_items:
			iconset = gtk.icon_factory_lookup_default(alias)
			iconfactory.add(item, iconset)

	iconfactory.add_default()

def get_image_path(image_id):
	imgname = image_id + '.png'
	imgpath = os.path.join(GENERIC_ICONS_PATH, imgname)
	if os.path.lexists(imgpath): return imgpath
	return None

def get_stock_pixbuf(image_id, size=FIXED16):
	return gtk.Image().render_icon(image_id, size)

def get_pixbuf(image_id, size=FIXED16):
	if image_id[:4] == 'gtk-':
		return get_stock_pixbuf(image_id, size)
	else:
		loader = gtk.gdk.pixbuf_new_from_file
		imgpath = get_image_path(image_id)
		if imgpath is None:
			return get_stock_pixbuf(gtk.STOCK_DELETE, size)
		return loader(imgpath)

def get_stock_image(image_id, size=FIXED16):
	image = gtk.Image()
	image.set_from_pixbuf(get_stock_pixbuf(image_id, size))
	return image

def get_image(image_id, size=FIXED16):
	if image_id[:4] == 'gtk-':
		return get_stock_image(image_id, size)
	else:
		image = gtk.Image()
		image.set_from_pixbuf(get_pixbuf(image_id))
		return image

def rgb_to_gdk_hexcolor(color):
	r, g, b = color
	return '#%04x%04x%04x' % (r * 65535.0, g * 65535.0, b * 65535.0)

def rgb_to_gdkcolor(color):
	return gtk.gdk.Color(rgb_to_gdk_hexcolor(color))

def gdk_hexcolor_to_rgb(hexcolor):
	r = int(hexcolor[1:5], 0x10) / 65535.0
	g = int(hexcolor[5:9], 0x10) / 65535.0
	b = int(hexcolor[9:], 0x10) / 65535.0
	return (r, g, b)

def gdkcolor_to_rgb(color):
	return gdk_hexcolor_to_rgb(color.to_string())

def rgb_to_gdkpixel(color):
	r, g, b = color
	r = int(r * 256);g = int(g * 256);b = int(b * 256)
	return r * 256 * 256 * 256 + g * 65536 + b * 256 + 255
