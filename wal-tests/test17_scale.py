import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		rb0 = wal.HScale(self)
		self.pack(rb0, padding=10)

	def callback(self, *args):
		print 'Changed!'

mw = MW()
mw.run()