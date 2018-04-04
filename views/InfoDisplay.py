from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View

class display(View):
    def __init__(self, parent):
        super().__init__(parent)

        self.loadMenu('config/display-menu.json')

        self.layout = QVBoxLayout()
        self.setViewLayout(self.layout)

        loadButton = QPushButton("Load Town")
        loadButton.clicked.connect(self.sig)
        self.layout.addWidget(loadButton)

    def sig(self):
        print("Heyo")
