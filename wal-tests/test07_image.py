import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.pack(wal.Image(self, wal.IMG_APP_ICON), padding=30)
		self.pack(wal.ActiveImage(self, wal.IMG_APP_ICON,
			tooltip='Active Image', cmd=self.callback), padding=30)

	def callback(self, button):
		if button == 1:print 'LEFT BUTTON'
		if button == 3:print 'RIGHT BUTTON'

mw = MW()
mw.run()
