import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		self.hor_box = wal.HidableHBox(self)
		self.pack(self.hor_box)

		size = (50, 50)

		self.hor_box.pack(wal.ColorPlate(self.hor_box, size, bg=wal.BLACK), True, True)
		self.hor_box.set_visible(True)

		hbox = wal.HBox(self)
		self.pack(hbox, True, True)

		self.vert_box = wal.HidableVBox(hbox)
		self.vert_box.pack(wal.ColorPlate(self.hor_box, size, bg=wal.GRAY), True, True)
		self.vert_box.set_visible(True)
		hbox.pack(self.vert_box)

		vbox = wal.VBox(hbox)
		hbox.pack(vbox, end=True)
		vbox.pack(wal.Button(vbox, 'Test HBox', cmd=self.test_hbox))
		vbox.pack(wal.Button(vbox, 'Test VBox', cmd=self.test_vbox))

	def test_hbox(self, *args):
		self.hor_box.set_visible(not self.hor_box.get_visible())

	def test_vbox(self, *args):
		self.vert_box.set_visible(not self.vert_box.get_visible())

mw = MW()
mw.run()
