import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		but = wal.ImageButton(self, wal.IMG_PALETTE_ARROW_BOTTOM, 'test')
		self.pack(but, padding=10)
		but = wal.FlatImageButton(self, wal.IMG_PALETTE_DOUBLE_ARROW_BOTTOM, 'test')
		self.pack(but, padding=10)

	def test(self, *args):print 'CLICKED!'


mw = MW()
mw.run()