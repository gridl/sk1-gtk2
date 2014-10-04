import wal

class MW(wal.MainWindow):

	def __init__(self):
		wal.MainWindow.__init__(self)
		wal.registry_aliases("_Don't save")
		self.set_size(300, 200)
		rb0 = wal.Button(self, 'Info', cmd=self.callback0)
		rb1 = wal.Button(self, 'Warning', cmd=self.callback1)
		rb2 = wal.Button(self, 'Error', cmd=self.callback2)
		rb3 = wal.Button(self, 'Info with details', cmd=self.callback3)
		rb4 = wal.Button(self, 'Warning with details', cmd=self.callback4)
		rb5 = wal.Button(self, 'Error with details', cmd=self.callback5)
		rb6 = wal.Button(self, 'Ask for save', cmd=self.callback6)
		rb7 = wal.Button(self, 'Yes-No', cmd=self.callback7)
		rb8 = wal.Button(self, 'Yes-No-Cancel', cmd=self.callback8)
		self.pack_all((rb0, rb1, rb2, rb3, rb4, rb5, rb6, rb7, rb8), padding=10)

	def callback0(self, *args):
		title = 'Info'
		first = 'It seems it\'s OK!'
		second = 'You can try continuing jobs.'
		wal.info_dialog(self, title, first, second)

	def callback1(self, *args):
		title = 'Warning'
		first = 'Well, the result fifty-fifty'
		second = 'Be careful in jobs.'
		wal.warning_dialog(self, title, first, second)

	def callback2(self, *args):
		title = 'Error'
		first = 'Oops! Sorry!'
		second = 'Jobs are impossible.'
		wal.error_dialog(self, title, first, second)

	def callback3(self, *args):
		title = 'Info'
		first = 'It seems it\'s OK!'
		second = 'You can try continuing jobs.'
		details = ('Some details', 'If a default button is not specified, \
		QMessageBox tries to find one based on the button roles of the buttons \
		used in the message box.')
		wal.info_dialog(self, title, first, second, details)

	def callback4(self, *args):
		title = 'Warning'
		first = 'Well, the result fifty-fifty'
		second = 'Be careful in jobs.'
		details = ('More info', 'The default button (i.e., the button activated \
		when Enter is pressed) can be specified using setDefaultButton().')
		wal.warning_dialog(self, title, first, second, details)

	def callback5(self, *args):
		title = 'Error'
		first = 'Oops! Sorry!'
		second = 'Jobs are impossible.'
		details = ('Error stacktrace', 'Note that the static function signatures \
		have changed with respect to their button parameters, which are now used \
		to set the standard buttons and the default button.')
		wal.error_dialog(self, title, first, second, details)

	def callback6(self, *args):
		title = 'Warning'
		first = 'The document <xxxxxxx yyyyy> has been changed!'
		second = 'Do you wish to save it?.'
		print wal.ask_save_dialog(self, title, first, second)

	def callback7(self, *args):
		title = 'Info'
		first = 'The document <xxxxxxx yyyyy> has been changed!'
		second = 'Do you wish to save it?.'
		print wal.yesno_dialog(self, title, first, second)

	def callback8(self, *args):
		title = 'Info'
		first = 'The document <xxxxxxx yyyyy> has been changed!'
		second = 'Do you wish to save it?.'
		print wal.yesnocancel_dialog(self, title, first, second)


mw = MW()
mw.run()
