from duplicity.log import add_file

__author__ = 'atila'

from gi.repository import Gtk

class V2MWindow:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ui/v2m.glade")

        handlers = {
            "onDeleteWindow": Gtk.main_quit,
            "on_window_destroy": self.on_window_destroy,
            "on_menu_about_activate": self.on_menu_about_activate,
            "on_menu_quit_activate": self.on_menu_quit_activate,
            "on_menu_delete_activate": self.on_menu_delete_activate,
            "on_menu_add_activate": self.on_menu_add_activate,
            "on_toolbutton_add_clicked": self.on_toolbutton_add_clicked
        }
        builder.connect_signals(handlers)

        self.window = builder.get_object("window")
        self.about_dialog = builder.get_object("aboutdialog")
        self.filechooser = builder.get_object("filechooserdialog")

    def on_window_destroy(self, widget):
        Gtk.main_quit()

    def on_menu_about_activate(self, widget):
        print "about"
        self.about_dialog.run()
        self.about_dialog.hide()

    def on_menu_quit_activate(self, widget):
        Gtk.main_quit()

    def on_menu_delete_activate(self, widget):
        print "delete item ..."

    def on_menu_add_activate(self, widget):
        self.add_files(widget)

    def on_toolbutton_add_clicked(self, widget):
        self.add_files(widget)

    def add_files(self, widget):
        print "add files ..."
        response = self.filechooser.run()
        if response == Gtk.ResponseType.OK:
            print "Open clicked"
            print "File selected: " + self.filechooser.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print "Cancel clicked"

        self.filechooser.hide()
