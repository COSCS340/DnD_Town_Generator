import sys
import random
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
        self.widgets['scrollarea'].setWidgetResizable(True)
        self.widgets['scrollarea'].setWidget(self.widgets['basescroller'])
        # CHANGED THIS
        self.layouts['main'].addWidget(self.widgets['scrollarea']) #needs to be basescroller
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
        j = 0
        for i in self.citizens:
            j += 1
            self.boxes[i] = QTextEdit(self)
            self.boxes[i].setStyleSheet("QTextEdit { background-color: rgb(211, 211, 211) }")
            self.boxes[i].setReadOnly(True)
            fullname = str(j) + '. ' + i.fname + ' ' + i.lname + '\n'

            if i.sex == 'm':
                sex = 'Male'
            else:
                sex = 'Female'
            fullname += '\tSex: ' + sex + '\n'

            if i.age == 0:
                rand = random.randint(1,12)
                age = str(rand) + ' Months'
            else:
                age = str(i.age) + ' Years'
            fullname += '\tAge: ' + age + '\n'
            fullname += '\tOccupation: ' + i.occupation + '\n'
            fullname += '\t Life Events: \n'
            for event in i.life:
                fullname += '\t\t' + event + '\n'
            self.boxes[i].setText(fullname)
            self.boxes[i].setFontPointSize(12)
            self.layouts['innerbox'].addWidget(self.boxes[i])
            self.widgets['scrollarea'].setWidget(self.widgets['basescroller'])
