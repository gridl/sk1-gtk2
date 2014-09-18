
import gtk
from sk1.widgets import SpinButton, SpinButtonInt

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

		spin = SpinButton(10, (0, 40), 0.2)
		self.pack_start(spin, False, False, 5)

		spin = SpinButtonInt(10, (0, 40), 2)
		self.pack_start(spin, False, False, 5)

TestWin().run()
