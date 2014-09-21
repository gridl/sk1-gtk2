
import gtk
from sk1 import events

class TestWin:

	def __init__(self):
		self.win = gtk.Window()
		self.win.connect('destroy', self.exit)

		self.win.add(Content())

		self.win.show_all()

	def run(self):
		gtk.main()

	def exit(self, *args):
		gtk.main_quit()

class Content(gtk.VBox):

	def __init__(self):
		gtk.VBox.__init__(self)

		but1 = gtk.Button('Subscribe')
		but1.connect('clicked', self.subscribe)
		self.pack_start(but1)

		but2 = gtk.Button('Send event')
		but2.connect('clicked', self.send_event)
		self.pack_start(but2)

		but3 = gtk.Button('Unsubscribe')
		but3.connect('clicked', self.unsubscribe)
		self.pack_start(but3)

	def subscribe(self, *args):
		events.connect(events.APP_STATUS, self.callback)
		print 'eventloop connected'

	def send_event(self, *args):
		events.emit(events.APP_STATUS)
		print 'event sent'

	def unsubscribe(self, *args):
		events.disconnect(events.APP_STATUS, self.callback)
		print 'eventloop disconnected'

	def callback(self, *args):
		print 'Got event', args



TestWin().run()
