__author__ = 'atila'

from gi.repository import Gtk

class CellRendererPixbufWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererPixbuf Example")

        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["New", Gtk.STOCK_NEW])
        self.liststore.append(["Open", Gtk.STOCK_OPEN])
        self.liststore.append(["Save", Gtk.STOCK_SAVE])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_pixbuf = Gtk.CellRendererPixbuf()

        column_pixbuf = Gtk.TreeViewColumn("Video", renderer_pixbuf, stock_id=1)
        treeview.append_column(column_pixbuf)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Name", renderer_text, text=0)
        treeview.append_column(column_text)

        self.add(treeview)

if __name__ == '__main__':
    win = CellRendererPixbufWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
