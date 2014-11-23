import wal

class TestDoc(wal.ColorPlate):

	txt = 'Caption'
	size = (200, 150)

	def __init__(self, master, color, txt=''):
		if txt: self.txt = txt
		wal.ColorPlate.__init__(self, master, self.size, color)

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		self.set_size(300, 200)
		self.box.set_border_width(10)

		hb = wal.HBox(self)
		hb.pack(wal.Button(hb, stock=wal.STOCK_ADD, cmd=self.add_cmd))
		hb.pack(wal.Button(hb, stock=wal.STOCK_REMOVE, cmd=self.remove_cmd))
		self.pack(hb)

		self.db = wal.DocBook(self, self.switch_cmd,
							self.close_cmd, wal.STOCK_FILE)

		self.dt = [
				TestDoc(self.db, wal.GRAY, 'GRAY'),
				TestDoc(self.db, wal.WHITE, 'WHITE'),
				TestDoc(self.db, wal.BLACK, 'BLACK'),
				TestDoc(self.db, wal.BLUE, 'BLUE'),
				TestDoc(self.db, wal.GREEN, 'GREEN'),
				]
		self.docs = []


		self.pack(self.db, True, True)

	def add_cmd(self):
		for doc in self.dt:
			if not doc in self.docs:
				self.db.add_doc(doc, doc.txt)
				self.docs.append(doc)
				break

	def remove_cmd(self):
		if self.docs:
			doc = self.db.get_active_page()
			self.db.remove_doc(doc)
			self.docs.remove(doc)

	def close_cmd(self, doc):
		self.db.remove_doc(doc)
		self.docs.remove(doc)

	def switch_cmd(self, doc):
		print doc

mw = MW()
mw.run()
