import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		pal = wal.ImgPlate(self, wal.STOCK_DIALOG_WARNING,
						wal.rc.FIXED128, bg=wal.GRAY)
		self.pack(pal, True, True, 20)

mw = MW()
mw.run()
