import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		hbox = wal.HBox(self)

		but = wal.ToggleButton(hbox, 'Test', cmd=self.test)
		hbox.pack(but, padding=10)

		but = wal.ToggleButton(hbox, 'FTest', cmd=self.test, flat=True)
		hbox.pack(but, padding=10)

		but = wal.ImgToggleButton(hbox, wal.IMG_PALETTE_ARROW_BOTTOM,
						tooltip='test', cmd=self.test)
		hbox.pack(but, padding=10)

		but = wal.ImgToggleButton(hbox, wal.IMG_PALETTE_DOUBLE_ARROW_BOTTOM,
						tooltip='test', cmd=self.test)
		hbox.pack(but, padding=10)
		self.pack(hbox)

	def test(self, *args):print 'CHANGED!'


mw = MW()
mw.run()
