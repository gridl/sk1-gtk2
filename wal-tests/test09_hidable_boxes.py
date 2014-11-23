import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		self.hbox = wal.HidableHBox(self)
		self.pack(self.hbox)

		size = (50, 50)

		self.hbox.pack(wal.ColorPlate(self.hbox, size, bg=wal.BLACK), True, True)
		self.hbox.set_visible(True)

		hbox = wal.HBox(self)
		self.pack(hbox, True, True)

		self.vbox = wal.HidableVBox(hbox)
		self.vbox.pack(wal.ColorPlate(self.hbox, size, bg=wal.GRAY), True, True)
		self.vbox.set_visible(True)
		hbox.pack(self.vbox)

		vbox = wal.VBox(hbox)
		hbox.pack(vbox, end=True)
		vbox.pack(wal.Button(vbox, 'Test HBox', cmd=self.test_hbox))
		vbox.pack(wal.Button(vbox, 'Test VBox', cmd=self.test_vbox))

	def test_hbox(self):
		self.hbox.set_visible(not self.hbox.get_visible())

	def test_vbox(self):
		self.vbox.set_visible(not self.vbox.get_visible())

mw = MW()
mw.run()
