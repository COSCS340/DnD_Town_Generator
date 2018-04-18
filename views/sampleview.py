from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View


class SampleView(View):
    def __init__(self, parent):
        super().__init__(parent)
        self.loadMenu('config/view1-menu.json')

        self.layout = QVBoxLayout()
        self.setViewLayout(self.layout)

        butt = QPushButton('PRESS ME')
        butt.clicked.connect(self.sig)
        self.layout.addWidget(butt)

    def sig(self):
        self.setStatus('CLICK')
