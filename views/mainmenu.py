""" This is the main menu for the generator. """

import sys
from utils.multiview import View
from PyQt5.QtWidgets import QGridLayout

class MainMenu(View):
    """ Class that contains opening screen of program. """
    def setup_view(self):
        """ Initialize window & data structures. """
        self.load_menu('config/main-menu.json')

        # set up dictionary of widgets and layouts to easily find.
        self.widgets = {}
        self.layouts = {}

    def setupInterface(self):
        self.layouts['main'] = QGridLayout()

        self.set_layout(self.layouts['main'])

    def sig(self):
        sys.exit()
