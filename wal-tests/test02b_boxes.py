import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		size = (50, 50)

		self.pack(wal.ColorPlate(self, size, bg=wal.BLACK))
		hbox = wal.HBox(self)
		hbox.pack(wal.ColorPlate(hbox, size, bg=wal.GRAY))
		self.pack(hbox)

mw = MW()
mw.run()
