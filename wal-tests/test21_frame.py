import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.box.set_border_width(10)

		size = (200, 150)

		frame = wal.Frame(self, 'Test Frame')
		cp = wal.ColorPlate(frame, size, wal.BLACK)
		frame.add(cp)
		self.pack(frame, padding=10)

		frame = wal.Frame(self)
		cp = wal.ColorPlate(frame, size, wal.BLUE)
		frame.add(cp)
		self.pack(frame, padding=10)

		frame = wal.Frame(self)
		cp = wal.ColorPlate(frame, size, wal.RED)
		frame.add(cp)
		check = wal.CheckButton(frame, 'Testing label')
		frame.set_label_widget(check)
		self.pack(frame, padding=10)

mw = MW()
mw.run()
