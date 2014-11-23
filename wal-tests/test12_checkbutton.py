import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.pack(wal.CheckButton(self, 'Selected', True, cmd=self.callback),
				padding=30)
		self.pack(wal.CheckButton(self, 'Not selected', False, cmd=self.callback),
				padding=30)

	def callback(self):
		print 'Changed!'

mw = MW()
mw.run()
