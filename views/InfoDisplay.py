import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View


class InfoDisplay(View):
    def setup_view(self):
        self.load_menu('config/display-menu.json')

        self.layouts = {}
        self.widgets = {}

        self.setupInterface()

    def setupInterface(self):
        self.layouts['main'] = QVBoxLayout()

        print(self.parent.access('wizard').town.citizens)
        # print(super().access('wizard').town.citizens)

        self.widgets['scrollarea'] = QScrollArea()

        self.layouts['main'].addWidget(self.widgets['scrollarea'])
        self.set_layout(self.layouts['main'])

    def sig(self):
        sys.exit()
