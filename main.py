import os
import sys
import json

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import MultiView

from views.townwizard import TownWizard
from views.sampleview import SampleView


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # hit the bars
        self.mb = self.menuBar()
        self.sb = self.statusBar()

        # houses custom view widgets
        # fancy stack widget
        self.mv = MultiView(self.mb, self.sb)
        self.mv.add_view('wizard', TownWizard(self.mv))
        self.mv.set_view('wizard')

        # create other widgets
        self.widgets = {}
        self.widgets['main'] = QWidget()
        self.widgets['home'] = QPushButton('Home')
        self.widgets['wizard'] = QPushButton('Wizard')

        # create a base layout
        self.layout = QGridLayout()

        # set the layout
        self.widgets['main'].setLayout(self.layout)

        # add to the layout
        self.layout.addWidget(self.widgets['home'], 0, 0)
        self.layout.addWidget(self.widgets['wizard'], 0, 1)
        self.layout.addWidget(self.mv.get_widget(), 1, 0, 1, 2)

        # set center
        self.setCentralWidget(self.widgets['main'])

        # show
        self.show()


if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)

    # initalize classes
    win = Main()

    # execute, clean up, and exit
    sys.exit(app.exec_())
