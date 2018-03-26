# test.py
# Author:  Ben Johnson
# Purpose: Provide a temporary wrapper for townwizard and also test
#          View/MultiView function

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
import json

from utils.multiview import MultiView
from views.townwizard import TownWizard
from views.sampleview import view1

class Test(MultiView):
    def __init__(self):
        # variables
        super().__init__()
        self.title = 'Implementation Tester'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 400

        self.createMenuBar()
        self.createStatusBar()

        # init
        self.initUI()

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # case widget
        self.case = QWidget()

        # layout
        self.layout = QGridLayout()
        self.case.setLayout(self.layout)

        self.home = view1(self)
        self.wiz = TownWizard(self)

        self.addView(self.home)
        self.addView(self.wiz)

        # real widgets
        butt = QPushButton('Home')
        butt.clicked.connect(self.homesig)
        butt2 = QPushButton('Wizard')
        butt2.clicked.connect(self.wizardsig)

        self.layout.addWidget(butt, 0,0)
        self.layout.addWidget(butt2, 0,1)
        self.layout.addWidget(self.getViewer(), 1,0,1,3)
        self.layout.setColumnStretch(2,4)

        self.setCurrentView(self.home)
        self.setCentralWidget(self.case)

    def homesig(self):
        if self.getCurrentView() != self.home.getWidget():
            self.setCurrentView(self.home)

    def wizardsig(self):
        if self.getCurrentView() != self.wiz.getWidget():
            self.setCurrentView(self.wiz)



if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)

    # initalize classes
    win = Test()

    # execute, clean up, and exit
    sys.exit(app.exec_())
