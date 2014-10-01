import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		self.area = wal.HidableVArea(self)
		self.area.pack(wal.ColorPlate(self.area, bg=wal.GRAY), True, True)
		self.pack(self.area, True, True)
		self.area.set_visible(True)

		self.pack(wal.Button(self, 'Test HidableArea', cmd=self.test_area), end=True)

	def test_area(self, *args):
		self.area.set_visible(not self.area.get_visible())

mw = MW()
mw.run()
