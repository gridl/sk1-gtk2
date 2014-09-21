
import gtk
import cairo

class TestCairo:

	def __init__(self):
		self.win = gtk.Window()
		self.win.connect('destroy', self.exit)
		self.win.set_default_size(550, 450)

		self.canvas = Canvas()
		self.win.add(self.canvas)

		self.win.show_all()

	def run(self):
		self.canvas.queue_draw()
		gtk.main()

	def exit(self, *args):
		gtk.main_quit()

CAIRO_WHITE = [1.0, 1.0, 1.0]

class Canvas(gtk.DrawingArea):

	start = end = []
	draw_flag = False
	block_flag = False
	image = None

	def __init__(self):
		gtk.DrawingArea.__init__(self)
		self.connect('expose_event', self.expose)
		self.add_events(gtk.gdk.BUTTON_PRESS_MASK |
					gtk.gdk.POINTER_MOTION_MASK |
					gtk.gdk.BUTTON_RELEASE_MASK |
	          		gtk.gdk.SCROLL_MASK)
		self.connect('button_press_event', self.mousePressEvent)
		self.connect('motion_notify_event', self.mouseMoveEvent)
		self.connect('button_release_event', self.mouseReleaseEvent)

	def expose(self, *args):
		ctx = self.window.cairo_create()
		x, y, w, h = self.allocation
		self.image = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
		image_ctx = cairo.Context(self.image)
		image_ctx.set_source_rgb(*CAIRO_WHITE)
		image_ctx.paint()
		image_ctx.set_source_rgb(0, 0, 0)
		image_ctx.rectangle(30, 40, 100, 200)
		image_ctx.fill()
		ctx.set_source_surface(self.image)
		ctx.paint()

	def draw(self):
		if self.draw_flag and self.start and self.end:
			self.block_flag = not self.block_flag
			ctx = self.window.cairo_create()
			x, y, w, h = self.allocation
			image = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
			image_ctx = cairo.Context(image)
			image_ctx.set_source_surface(self.image)
			image_ctx.paint()
			x0, y0 = self.start
			x1, y1 = self.end

			image_ctx.set_antialias(cairo.ANTIALIAS_NONE)
			image_ctx.set_operator(cairo.OPERATOR_ADD)

			image_ctx.set_source_rgb(0, 0, 0)
			image_ctx.set_dash([5, 5])
			image_ctx.set_line_width(1)
			image_ctx.rectangle(x0, y0, x1 - x0, y1 - y0)
			image_ctx.stroke()

			image_ctx.set_antialias(cairo.ANTIALIAS_DEFAULT)
			image_ctx.set_operator(cairo.OPERATOR_OVER)

			ctx.set_source_surface(image)
			ctx.paint()
			self.block_flag = not self.block_flag

	def mousePressEvent(self, widget, event):
		self.start = [event.x, event.y]
		self.draw_flag = True

	def mouseMoveEvent(self, widget, event):
		if not self.block_flag:
			self.draw()
			self.end = [event.x, event.y]
			self.draw()

	def mouseReleaseEvent(self, widget, event):
		self.draw()
		self.draw_flag = False
		self.end = self.start = []



app = TestCairo()
app.run()
