import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.pack(wal.HLine(self), padding=30)
		hbox = wal.HBox(self)
		hbox.pack(wal.VLine(self), True, True)
		self.pack(hbox, True, True)

mw = MW()
mw.run()
