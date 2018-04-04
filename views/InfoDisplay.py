from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View

class display(View):
    def __init__(self, parent):
        super().__init__(parent)

        self.loadMenu('config/display-menu.json')

    def sig(self):
        print("Heyo")
