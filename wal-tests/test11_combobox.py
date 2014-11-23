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
		self.pack(self.combo, padding=5)

		self.comboentry = wal.ComboBoxEntry(self, TEST_LIST,
										cmd=self.test_comboentry)
		self.pack(self.comboentry, padding=5)

		self.comboentry2 = wal.ComboBoxEntry(self, TEST_LIST, editable=True,
										cmd=self.test_comboentry2)
		self.pack(self.comboentry2, padding=5)

	def test_combo(self):
		print 'Active index', self.combo.get_active()

	def test_comboentry(self):
		print 'Active index', self.comboentry.get_active()
		print 'Active text', self.comboentry.get_text()
		print 'State', self.comboentry.get_editable()

	def test_comboentry2(self):
		print 'Active index', self.comboentry2.get_active()
		print 'Active text', self.comboentry2.get_text()
		print 'State', self.comboentry2.get_editable()

mw = MW()
mw.run()
