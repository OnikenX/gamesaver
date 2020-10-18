import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        #title window
        Gtk.Window.__init__(self, title="GameSaver")
        #Button
        self.button = Gtk.Button(label="Click Here")
        #treat event
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        self.main()
    def on_button_clicked(self, widget):
        print("Hello World")


window = MainWindow()
