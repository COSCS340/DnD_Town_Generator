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
        butt = QPushButton('Home')
        butt.clicked.connect(self.homesig)
        butt2 = QPushButton('Wizard')
        butt2.clicked.connect(self.wizardsig)

        self.layout.addWidget(butt, 0,0)
        self.layout.addWidget(butt2, 0,1)
        self.layout.addWidget(self.getViewer(), 1,0,1,3)
        self.layout.setColumnStretch(2,4)

        self.setCurrentView(self.v1)
        self.setCentralWidget(self.case)

    def homesig(self):
        if self.getCurrentView() != self.v1.getWidget():
            self.setCurrentView(self.v1)

    def wizardsig(self):
        if self.getCurrentView() != self.v2.getWidget():
            self.setCurrentView(self.v2)

class view1(View):
    def __init__(self, parent):
        super().__init__(parent)
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
