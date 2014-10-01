import wal

class Plate(wal.ActiveColorPlate):

	bg = ()

	def __init__(self, master, size=(), bg=()):
		wal.ActiveColorPlate.__init__(self, master, size, bg)

	def mouse_enter(self, event):
		self.bg = self.get_bgcolor()
		self.set_bgcolor(wal.WHITE)

	def mouse_move(self, event): print 'MOVE!'
	def mouse_leave(self, event): self.set_bgcolor(self.bg)
	def mouse_left_down(self, event): self.set_bgcolor(wal.RED)
	def mouse_left_up(self, event): self.set_bgcolor(wal.WHITE)
	def mouse_right_down(self, event): self.set_bgcolor(wal.GREEN)
	def mouse_right_up(self, event): self.set_bgcolor(wal.WHITE)
	def mouse_left_dclick(self, event): self.set_bgcolor(wal.BLACK)
	def mouse_middle_down(self, event): self.set_bgcolor(wal.YELLOW)
	def mouse_middle_up(self, event): self.set_bgcolor(wal.WHITE)
	def mouse_wheel(self, event):
		chnl = self.get_bgcolor()[0]
		chnl += event.direction * .05
		if chnl > 1.0: chnl = 1.0
		if chnl < 0.0: chnl = 0.0
		self.set_bgcolor((chnl, chnl, chnl))


class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		size = (100, 100)
		hbox = wal.HBox(self)
		self.pack(hbox, padding=10)
		hbox.pack(Plate(hbox, size), padding=10)

mw = MW()
mw.run()
