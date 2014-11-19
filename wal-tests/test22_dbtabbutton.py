import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.box.set_border_width(10)

		self.dbbutton = wal.DBTabButton(self)

		self.pack(self.dbbutton)

mw = MW()
mw.run()