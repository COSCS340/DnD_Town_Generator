import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
import json

from utils.multiview import MultiView
from views.townwizard import TownWizard
from views.sampleview import view1

class TG(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Implementation Tester'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 400

        # make menu and status bars
        self.menub = self.menuBar()
        self.statusb = self.statusBar()

        # make a multiview that changes menu/status bars
        self.mv1 = MultiView(self.menub, self.statusb)
        self.mv2 = MultiView(None, self.statusb)

        # make a view (TownWizard inherits View)
        # also make parent the MultiView for changing bars
        self.view11 = TownWizard(self.mv1)
        self.view12 = view1(self.mv1)
        self.view21 = TownWizard(self.mv2)
        self.view22 = view1(self.mv2)

        # make some switchy bois
        self.butt1 = QPushButton('Toggle view 1')
        self.butt2 = QPushButton('Toggle view 2')

        self.butt1.clicked.connect(self.sig1)
        self.butt2.clicked.connect(self.sig2)

        # associate views with the MultiViews
        self.mv1.addView(self.view11)
        self.mv1.addView(self.view12)

        self.mv2.addView(self.view21)
        self.mv2.addView(self.view22)

        # set the current view
        # NOTE: to not update menu bar, use extra param False
        self.mv1.setCurrentView(self.view11)
        self.mv2.setCurrentView(self.view22)

        # create a layout to show the views
        self.layout = QVBoxLayout()

        # add the multiviews
        self.layout.addWidget(self.butt1)
        self.layout.addWidget(self.butt2)
        self.layout.addWidget(self.mv1.getViewer())
        self.layout.addWidget(self.mv2.getViewer())

        # create a widget to show it
        self.case = QWidget()
        self.case.setLayout(self.layout)

        # add it to the window
        self.setCentralWidget(self.case)

        self.show()

    def sig1(self):
        if self.mv1.getCurrentView() == self.view11.getWidget():
            self.mv1.setCurrentView(self.view12)
        else: self.mv1.setCurrentView(self.view11)

    def sig2(self):
        if self.mv2.getCurrentView() == self.view21.getWidget():
            self.mv2.setCurrentView(self.view22)
        else: self.mv2.setCurrentView(self.view21)

if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)

    # initalize classes
    win = TG()

    # execute, clean up, and exit
    sys.exit(app.exec_())
