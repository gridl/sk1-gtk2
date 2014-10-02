import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.pack(wal.Label(self, 'Test Label'), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', italic=True), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', italic=True, bold=True), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', bold=True), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', size=-1), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', size=1), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', size=1, bold=True), padding=10)
		self.pack(wal.DecorLabel(self, 'Test DecorLabel', enabled=False), padding=10)
		self.pack(wal.URL_Label(self, 'http://sk1project.org'), padding=10)
		self.pack(wal.URL_Label(self, 'http://inkscape.org', tooltip='Home site'), padding=10)

mw = MW()
mw.run()
