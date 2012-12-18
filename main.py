__author__ = 'atila'

from gi.repository import Gtk
import V2MWindow

if __name__ == '__main__':
    v2m = V2MWindow.V2MWindow()
    v2m.window.show_all()
    Gtk.main()
