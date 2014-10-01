import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		size = (100, 50)
		cp1 = wal.ColorPlate(self, size, wal.BLACK)
		cp2 = wal.ColorPlate(self, size, wal.GRAY)
		cp3 = wal.ColorPlate(self, size, wal.WHITE)
		cp4 = wal.ColorPlate(self, size, wal.RED)
		cp5 = wal.ColorPlate(self, size, wal.GREEN)
		cp6 = wal.ColorPlate(self, size, wal.BLUE)

		self.pack_all((cp1, cp2, cp3, cp4, cp5, cp6), padding=10)

mw = MW()
mw.run()
