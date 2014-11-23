import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		hbox = wal.HBox(self)
		self.pack(hbox)
		self.cb1 = wal.ColorButton(hbox, (0, 0, 0), 'Select foreground',
								cmd=self.callback)
		hbox.pack(self.cb1, padding=30)
		self.cb2 = wal.ColorButton(hbox, (1, 1, 1), 'Select background',
								cmd=self.callback)
		hbox.pack(self.cb2, padding=30)

	def callback(self):
		print 'Changed!'
		print self.cb1.get_color()
		print self.cb2.get_color()

mw = MW()
mw.run()
