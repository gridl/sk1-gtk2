import wal

TEST_LIST = [
'Item 0',
'Item 1',
'Item 2',
'Item 3',
'Item 4',
'Item 5',
'Item 6',
]

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)

		self.combo = wal.ComboBoxText(self, TEST_LIST, cmd=self.test_combo)
		self.pack(self.combo)


	def test_combo(self, *args):
		print 'Active index', self.combo.get_active()

mw = MW()
mw.run()
