
import gtk

class TestWin:

	def __init__(self):
		self.win = gtk.Window()
		self.win.connect('destroy', self.exit)
		self.win.set_default_size(550, 450)

		self.win.add(Content())

		self.win.show_all()

	def run(self):
		gtk.main()

	def exit(self, *args):
		gtk.main_quit()

class Content(gtk.VBox):

	def __init__(self):
		gtk.VBox.__init__(self)



TestWin().run()
