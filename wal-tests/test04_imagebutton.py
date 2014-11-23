import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		hbox = wal.HBox(self)

		but = wal.ImgButton(hbox, wal.STOCK_ADD,
						tooltip='test', cmd=self.test)
		hbox.pack(but, padding=10)

		but = wal.ImgButton(hbox, wal.STOCK_EDIT,
						tooltip='test', cmd=self.test, flat=True)
		hbox.pack(but, padding=10)
		self.pack(hbox)

	def test(self):print 'CLICKED!'


mw = MW()
mw.run()
