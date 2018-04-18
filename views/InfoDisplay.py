import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View


class InfoDisplay(View):
    def setup_view(self):
        self.load_menu('config/display-menu.json')

        self.layouts = {}
        self.widgets = {}

        self.citizens = self.parent.access('wizard').town.citizens

        self.setupInterface()

    def setupInterface(self):
        # widgets
        self.widgets['scrollarea'] = QScrollArea()
        self.widgets['test'] = QPushButton('Press me')

        self.widgets['test'].clicked.connect(self.update_list)

        # layouts
        self.layouts['main'] = QVBoxLayout()
        self.set_layout(self.layouts['main'])

        # build
        self.layouts['main'].addWidget(self.widgets['scrollarea'])
        self.layouts['main'].addWidget(self.widgets['test'])

    def sig(self):
        sys.exit()

    # function to call when town created
    def update_list(self):
        for i in self.citizens:
            print(f'{i.fname} {i.lname}')
