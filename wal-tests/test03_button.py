import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		but = wal.Button(self, 'Test button', cmd=self.test)
		self.pack(but)

	def test(self, *args):print 'CLICKED!'


mw = MW()
mw.run()
