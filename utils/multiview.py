'''
The purpose of View/MultiView is to easily create separate widgets that can
all work together to the benefit of one program

Individual widgets inherit View and have the ability to set status bar messages
and menus without the knowledge of the actual status bar

The main script runs a MultiView object and passes the bars to the call (if you
want) or inherits it
'''


import sys
import os
import json

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *


class MultiView(QWidget):
    def __init__(self, menubar, statusbar):
        super().__init__()
        self.menubar = menubar
        self.statusbar = statusbar
        self.MultiViewWidget = QStackedWidget()
        self.current_view = None
        self.menu = {}
        self.views = {}

    def add_view(self, name, view):
        self.views[name] = view
        self.MultiViewWidget.addWidget(view.get_widget())

    def set_view(self, name, update_menu=True):
        if name in self.views:
            self.MultiViewWidget.setCurrentWidget(
                self.views[name].get_widget()
            )
            self.current_view = self.views[name]
        if update_menu:
            self.set_menu(self.views[name].get_menu())

    def get_widget(self):
        return self.MultiViewWidget

    def set_menu(self, menu):
        if self.menubar is not None and menu is not None:
            # clear menu things
            self.menubar.clear()
            self.menu.clear()

            # build up menu
            for m in menu:
                self.menu[m] = {}
                tmp = self.menubar.addMenu(m)
                for s in menu[m]:
                    if 'separator' in menu[m][s]:
                        tmp.addSeparator()
                        continue
                    hotkey = ''
                    if 'hotkey' in menu[m][s]:
                        hotkey = menu[m][s]['hotkey']
                    self.menu[m][s] = QtWidgets.QAction(s, self,
                                                        shortcut=hotkey)
                    if 'signal' in menu[m][s]:
                        self.menu[m][s].triggered.connect(
                            getattr(self.current_view, menu[m][s]['signal']))
                    if 'disabled' in menu[m][s]:
                        if menu[m][s]['disabled'] == "True":
                            self.menu[m][s].setDisabled(True)
                    tmp.addAction(self.menu[m][s])


class View(QWidget):
    def __init__(self, multiview):
        super().__init__()

        self.parent = multiview
        self.ViewMainWidget = QWidget()
        self.ViewMainMenu = None

        self.setup_view()

    def load_menu(self, filename):
        self.ViewMainMenu = json.load(open(filename))

    def set_layout(self, layout):
        self.ViewMainWidget.setLayout(layout)

    def get_widget(self):
        return self.ViewMainWidget

    def get_menu(self):
        if self.ViewMainMenu is not None:
            return self.ViewMainMenu

    def update_menu(self):
        if self.ViewMainMenu is not None:
            self.parent.set_menu(self.get_menu())

    def set_status(self, string):
        self.parent.statusbar.showMessage(string)


'''
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

    def updateMenu(self):
        self.mvp.setmenu(self.getMenu())

    def getWidget(self):
        return self.ViewMainWindow

    def setViewLayout(self, layout):
        self.ViewMainWidget.setLayout(layout)

    def setStatus(self, mess):
        self.mvp.statusbar.showMessage(mess)

class MultiView(QtWidgets.QMainWindow):
    def __init__(self, menub=None, statusb=None):
        # variables
        super().__init__()
        self.MultiViewWidget = QStackedWidget()
        self.menub = menub
        self.statusbar = statusb
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

    def createMenuBar(self):
        self.menub = self.menuBar()
    def createStatusBar(self):
        self.statusbar = self.statusBar()

    # Current limitation (probably not a big deal):
    #   cannot dynamically add to the menu
    def setmenu(self, menu):
        if self.menub != None:
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
                    if 'disabled' in menu[m][s]:
                        if menu[m][s]['disabled'] == "True": self.menu[m][s].setDisabled(True)
                    tmp.addAction(self.menu[m][s])
'''
