import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from utils.multiview import View


class InfoDisplay(View):
    def setup_view(self):
        self.load_menu('config/display-menu.json')

        self.layouts = {}
        self.widgets = {}
        self.boxes ={}

        self.citizens = self.parent.access('wizard').town.citizens

        self.setupInterface()

    def setupInterface(self):
        # widgets
        self.widgets['scrollarea'] = QScrollArea()
        self.widgets['refresh'] = QPushButton('Refresh')

        self.widgets['refresh'].clicked.connect(self.refresh)

        # layouts
        self.layouts['main'] = QVBoxLayout()
        self.set_layout(self.layouts['main'])

        self.layouts['innerbox'] = QVBoxLayout()
        self.widgets['scrollarea'].setWidget(self.layouts['innerbox'].widget())

        # build
        self.layouts['main'].addWidget(self.widgets['scrollarea'])
        self.layouts['main'].addWidget(self.widgets['refresh'])

    def sig(self):
        sys.exit()

    # function to call when town created
    def refresh(self):
        self.citizens = self.parent.access('wizard').town.citizens
        for i in self.citizens:
            self.boxes[i] = QTextEdit(self)
            self.boxes[i].setTextBackgroundColor(QColor(128, 128, 128))
            self.boxes[i].setText(f'{i.fname} {i.lname}')
            self.layouts['innerbox'].addWidget(self.boxes[i])
