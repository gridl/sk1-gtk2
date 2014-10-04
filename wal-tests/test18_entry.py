import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.txt0 = wal.Entry(self, 'Red', cmd=self.callback,
							check_focus=True, check_enter=True)
		txt1 = wal.Entry(self, 'Green')
		txt2 = wal.Entry(self, 'Blue')
		txt1.set_sensitive(False)
		txt2.set_editable(False)
		self.pack_all((self.txt0, txt1, txt2), padding=10)

	def callback(self, *args):
		print self.txt0.get_text()

mw = MW()
mw.run()