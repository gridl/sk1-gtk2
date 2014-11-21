import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.box.set_border_width(10)

		self.nb = wal.NoteBook(self)

		size = (200, 150)

		cp1 = wal.ColorPlate(self.nb, size, wal.BLACK)
		tablabel = wal.DBTabLabel(self.nb, cp1, 'BLACK',
								cmd=self.close_cmd, icon_id=wal.STOCK_ABOUT)
		self.nb.add_page(cp1, tab_label=tablabel)
		cp2 = wal.ColorPlate(self.nb, size, wal.GRAY)
		self.nb.add_page(cp2, 'GRAY')
		cp3 = wal.ColorPlate(self.nb, size, wal.WHITE)
		self.nb.add_page(cp3, 'WHITE')

		self.pack(self.nb)

	def close_cmd(self, doc):
		print doc

mw = MW()
mw.run()
