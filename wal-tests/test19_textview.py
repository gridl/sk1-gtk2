import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		txt0 = wal.TextView(self, 'Red')
		txt1 = wal.TextView(self, 'Green')
		txt2 = wal.TextView(self, 'Blue')
		txt1.set_sensitive(False)
		txt2.set_editable(False)
		self.pack_all((txt0, txt1, txt2), padding=10)


mw = MW()
mw.run()