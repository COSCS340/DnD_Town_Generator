import sys, os, json
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

class View(QWidget):
    def __init__(self, mvp):
        super().__init__()

        # da real Multi View Parent
        self.mvp = mvp
        self.ViewMainWindow = QWidget()
        self.ViewMainMenu = {}

    def loadMenu(self, fn):
        self.ViewMainMenu = json.load(open(fn))

    def getMenu(self):
        return self.ViewMainMenu

    def getWidget(self):
        return self.ViewMainWindow

    def setViewLayout(self, layout):
        self.ViewMainWindow.setLayout(layout)

    def setStatus(self, mess):
        self.mvp.statusbar.showMessage(mess)

class MultiView(QtWidgets.QMainWindow):
    def __init__(self):
        # variables
        super().__init__()
        self.MultiViewWidget = QStackedWidget()
        self.menub = self.menuBar()
        self.statusbar = self.statusBar()
        self.menu = {}

    def addView(self, v):
        self.MultiViewWidget.addWidget(v.getWidget())

    def setCurrentView(self, v, updatemenu=True):
        self.currView = v
        self.MultiViewWidget.setCurrentWidget(v.getWidget())
        if updatemenu: self.setmenu(v.getMenu())

    def getCurrentView(self):
        return self.MultiViewWidget.currentWidget()

    def getViewer(self):
        return self.MultiViewWidget

    # Current limitation (probably not a big deal):
    #   cannot dynamically add to the menu
    def setmenu(self, menu):
        # clear menu things
        self.menub.clear()
        self.menu.clear()

        # build up menu
        for m in menu:
            self.menu[m] = {}
            tmp = self.menub.addMenu(m)
            for s in menu[m]:
                if 'separator' in menu[m][s]:
                    tmp.addSeparator()
                    continue
                hotkey = ''
                if 'hotkey' in menu[m][s]:
                    hotkey = menu[m][s]['hotkey']
                self.menu[m][s] = QtWidgets.QAction(s, self, shortcut=hotkey)
                if 'signal' in menu[m][s]:
                    self.menu[m][s].triggered.connect(getattr(self.currView, menu[m][s]['signal']))
                tmp.addAction(self.menu[m][s])
