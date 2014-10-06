import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.box.set_border_width(10)

		self.nb = wal.NoteBook(self)

		size = (200, 150)
		cp1 = wal.ColorPlate(self.nb, size, wal.BLACK)
		self.nb.add_page(cp1, 'BLACK')
		cp2 = wal.ColorPlate(self.nb, size, wal.GRAY)
		self.nb.add_page(cp2, 'GRAY')
		cp3 = wal.ColorPlate(self.nb, size, wal.WHITE)
		self.nb.add_page(cp3, 'WHITE')
		cp4 = wal.ColorPlate(self.nb, size, wal.RED)
		self.nb.add_page(cp4, 'RED')
		cp5 = wal.ColorPlate(self.nb, size, wal.GREEN)
		self.nb.add_page(cp5, 'GREEN')
		cp6 = wal.ColorPlate(self.nb, size, wal.BLUE)
		self.nb.add_page(cp6, 'BLUE')

		self.pack(self.nb)

mw = MW()
mw.run()
