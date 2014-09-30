import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		hbox = wal.HBox(self)
		self.pack(hbox, padding=30)
		self.sb1 = wal.SpinButton(hbox, rng=(0.0, 10.0), cmd=self.callback,
								check_focus=True)
		hbox.pack(self.sb1, padding=30)

		self.sb2 = wal.SpinButtonInt(hbox, rng=(-10, 20), cmd=self.callback,
								check_focus=True)
		hbox.pack(self.sb2, padding=30)

	def callback(self, *args):
		print 'Changed!'
		print self.sb1.get_value()
		print self.sb2.get_value()

mw = MW()
mw.run()
