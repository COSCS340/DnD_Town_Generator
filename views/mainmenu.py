""" This is the main menu for the generator. """

import sys
from PyQt5.QtWidgets import QGridLayout, QLabel, QLayoutItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QIcon, QPixmap, QFont
from utils.multiview import View


class MainMenu(View):
    """ Class that contains opening screen of program. """
    def setup_view(self):
        """ Initialize window & data structures. """
        self.load_menu('config/main-menu.json')

        # set up dictionary of widgets and layouts to easily find.
        self.widgets = {}
        self.layouts = {}
        self.setupInterface()

    def setupInterface(self):
        self.layouts['main'] = QGridLayout()

        self.widgets['welcomelabel'] = QLabel("Welcome! "
                                              "To begin, load your town "
                                              "into the wizard, or click help")
        font = QFont("Arial", 18)
        self.widgets['welcomelabel'].setFont(font)

        self.widgets['image'] = QLabel()
        pixmap = QPixmap('img/dnd4_resized.png')
        self.widgets['image'].setPixmap(pixmap)
        self.widgets['image'].setAlignment(Qt.AlignCenter)

        self.layouts['main'].addWidget(self.widgets['welcomelabel'], 0, 1)
        self.layouts['main'].addWidget(self.widgets['image'], 1, 1,)
        self.layouts['main'].setColumnStretch(0, 1)
        self.layouts['main'].setColumnStretch(2, 1)
        self.layouts['main'].setRowStretch(2, 1)

        self.set_layout(self.layouts['main'])

    def sig(self):
        sys.exit()
