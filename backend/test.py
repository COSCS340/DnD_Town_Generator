import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
import json
from multiview import View, MultiView
from townwizardwid import Wizard

class Test(MultiView):
    def __init__(self):
        # variables
        super().__init__()
        self.title = 'Implementation Tester'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 400

        # init
        self.initUI()

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.menu = {}
        self.menub = self.menuBar()

        # case widget
        self.case = QWidget()

        # layout
        self.layout = QGridLayout()
        self.case.setLayout(self.layout)

        self.v1 = view1(self)
        self.v2 = Wizard(self)

        self.addView(self.v1)
        self.addView(self.v2)

        # real widgets
        butt = QPushButton('PRESS ME TO TOGGLE VIEWS')
        butt.clicked.connect(self.switchsig)

        self.layout.addWidget(butt, 0,0)
        self.layout.addWidget(self.getViewer(), 1,0)

        self.setCurrentView(self.v1)
        self.setCentralWidget(self.case)

    def switchsig(self):
        if self.getCurrentView() == self.v1.getWidget():
            self.setCurrentView(self.v2)
        else: self.setCurrentView(self.v1)

class view1(View):
    def __init__(self, parent):
        super().__init__()
        self.loadMenu('view1-menu.json')

        self.layout = QVBoxLayout()
        self.setViewLayout(self.layout)

        butt = QPushButton('PRESS ME')
        #butt.clicked.connect(parent.setCurrentWin(parent.v2))
        self.layout.addWidget(butt)

    def opensig(self):
        print('VIEW 1 OPEN CLICK')

if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)

    # initalize classes
    win = Test()

    # execute, clean up, and exit
    sys.exit(app.exec_())
