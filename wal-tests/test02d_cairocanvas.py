import wal

class Canvas(wal.CairoCanvas):

	bg = ()

	def __init__(self, master, size=(), bg=(), has_tooltip=False):
		wal.CairoCanvas.__init__(self, master, size, bg, has_tooltip)

	def repaint(self):
		self.clear()
		rect = (10, 10, 30, 20)
		self.rectangle(rect, wal.RED, wal.DARK_GREEN, 4)
		points = [(10, 20), (30, 20), (10, 40), (60, 70), (100, 20), (60, 200), ]
		self.polyline(points, wal.GRAY, 3)

	def update_tooltip(self, x, y):
		return (wal.STOCK_ABOUT, 'CairoCanvas', 'sK1 WAL edition')



class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		size = (200, 150)
		hbox = wal.HBox(self)
		self.pack(hbox, padding=10)
		hbox.pack(Canvas(hbox, size, wal.WHITE, True), padding=10)

mw = MW()
mw.run()
