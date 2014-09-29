import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		hbox = wal.HBox(self)
		self.pack(hbox)
		hbox.pack(wal.ColorButton(hbox, (0, 0, 0), 'Select foreground',
								cmd=self.callback), padding=30)
		hbox.pack(wal.ColorButton(hbox, (1, 1, 1), 'Select background',
								cmd=self.callback), padding=30)

	def callback(self, *args):
		print 'Changed!'

mw = MW()
mw.run()
