import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		rb0 = wal.RadioButton(self, 'Red', None, True, cmd=self.callback)
		rb1 = wal.RadioButton(self, 'Green', rb0, False, cmd=self.callback)
		rb2 = wal.RadioButton(self, 'Blue', rb0, False, cmd=self.callback)
		self.pack_all((rb0, rb1, rb2), padding=10)

	def callback(self, *args):
		print 'Changed!'

mw = MW()
mw.run()
