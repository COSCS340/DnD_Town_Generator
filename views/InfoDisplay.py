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
        self.widgets['basescroller'] = QWidget()
        self.widgets['refresh'] = QPushButton('Refresh')

        self.widgets['refresh'].clicked.connect(self.refresh)

        # layouts
        self.layouts['main'] = QVBoxLayout()
        self.set_layout(self.layouts['main'])

        self.layouts['innerbox'] = QVBoxLayout()
        self.widgets['basescroller'].setLayout(self.layouts['innerbox'])

        # build
        self.widgets['scrollarea'].setWidgetResizable(False)
        self.layouts['innerbox'].addWidget(QLabel('dogs'))
        self.layouts['innerbox'].addWidget(QLabel('dogs'))
        self.layouts['innerbox'].addWidget(QLabel('dogs'))
        self.layouts['innerbox'].addWidget(QLabel('dogs'))
        self.widgets['scrollarea'].setWidget(self.widgets['basescroller'])
        # CHANGED THIS
        self.layouts['main'].addWidget(self.widgets['basescroller'])
        self.layouts['main'].addWidget(self.widgets['refresh'])

        # print(QtGlobal.qreal(12))

    def sig(self):
        sys.exit()

    # function to call when town created
    def refresh(self):
        print('here')

        if self.citizens == []:
            self.parent.statusbar.showMessage("Nothing in town.")
            return
        else:
            self.parent.statusbar.showMessage('')
        for i in self.citizens:
            self.boxes[i] = QTextEdit(self)
            self.boxes[i].setTextBackgroundColor(QColor(128, 128, 128))
            self.boxes[i].setReadOnly(True)
            fullname = i.fname + ' ' + i.lname
            self.boxes[i].setText(fullname)
            self.boxes[i].setFontPointSize(12)
            self.layouts['innerbox'].addWidget(self.boxes[i])
            self.widgets['scrollarea'].setWidget(self.widgets['basescroller'])
