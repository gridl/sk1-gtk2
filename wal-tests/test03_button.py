import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		but = wal.Button(self, 'Test button', cmd=self.test)
		but.connect('button-press-event', self.pressed)
		self.pack(but, padding=10)

	def test(self, *args):print 'CLICKED!'
	def pressed(self, *args):print 'PRESSED'


mw = MW()
mw.run()
