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
        self.menubar.setNativeMenuBar(False)
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

    def access(self, name):
        if name in self.views:
            return self.views[name]

    def set_menu(self, menu):
        if self.menubar is not None and menu is not None:
            # clear menu things
            self.menubar.clear()
            self.menu.clear()

            # build up menu
            for m in menu:
                self.menubar.addAction(menu[m].menuAction())

            '''
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
            '''


class View(QWidget):
    def __init__(self, multiview):
        super().__init__()

        self.parent = multiview
        self.ViewMainWidget = QWidget()
        self.ViewMainMenu = None

        self.setup_view()

    def load_menu(self, filename):
        # get structure
        with open(filename) as f:
            data = json.load(f)

        # build menu actions and stuff
        self.ViewMainMenu = {}

        for m in data:
            tmenu = QMenu(m)

            # build the submenu stuff
            for item in data[m]:
                # if separator
                if 'separator' in data[m][item]:
                    tmenu.addSeparator()
                    continue

                # options
                sig = None
                hotkey = ''

                if 'signal' in data[m][item]:
                    sig = getattr(self, data[m][item]['signal'])
                if 'hotkey' in data[m][item]:
                    hotkey = data[m][item]['hotkey']

                # build the action
                taction = QAction(item, tmenu, shortcut=hotkey)
                if sig is not None:
                    taction.triggered.connect(sig)

                # add to menu
                tmenu.addAction(taction)

            # add the menu
            self.ViewMainMenu[m] = tmenu

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
