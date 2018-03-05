# Town Wizard
# Purpose: A wizard (joke completely intended) to aid in the
#          compilation of town elements
# Author:  Ben Johnson


import os, sys, glob
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from town import Town
from changes import Changes
from multiview import View


class TownWizard(View):
    def __init__(self, mvp):
        # variables
        super().__init__(mvp)
        self.loadMenu('wiz-menu.json')

        # init
        self.initUI()

    def initUI(self):
        # variables
        self.models = {}
        self.widgets = {}
        self.layouts = {}
        self.menu = {}
        self.undo = []
        self.redo = []
        self.town = Town()
        self.changes = Changes()

        self.town.new()

        # add elements and setup layout
        self.setupInterface()

    def setupInterface(self):
        # widgets
        self.widgets['stack'] = QStackedWidget(self)
        self.widgets['tree'] = QTreeView()
        self.widgets['stagebox'] = QGroupBox('Staging Area')
        self.widgets['stage'] = QListWidget()
        self.widgets['new'] = QPushButton('New')
        self.widgets['edit'] = QPushButton('Edit')
        self.widgets['add'] = QPushButton('Add')
        self.widgets['townlabel'] = QLabel(self)
        self.widgets['info'] = {}
        self.widgets['info']['object'] = QGroupBox('Stats')
        self.widgets['info']['townlabel'] = QLabel(self)
        self.widgets['info']['towntext'] = QLineEdit(self)
        self.widgets['info']['peoplelabel'] = QLabel(self)
        self.widgets['info']['eventlabel'] = QLabel(self)
        self.widgets['info']['build'] = QPushButton('Build Town')

        # layouts
        self.layouts['main'] = QGridLayout()
        self.layouts['towninfo'] = QGridLayout()
        self.layouts['stage'] = QVBoxLayout()

        # switchy boi
        self.layouts['case'] = QVBoxLayout()
        self.switcher = QStackedWidget()
        #self.layouts['case'].addWiget(self.switcher) # STOPPED HERE
        # set view layout
        self.setViewLayout(self.layouts['main'])

        # sub-layouts
        self.widgets['stagebox'].setLayout(self.layouts['stage'])
        self.widgets['info']['object'].setLayout(self.layouts['towninfo'])

        # models
        self.models['tree'] = QFileSystemModel()

        ### widget setup ###

        # town name label widget setup
        self.widgets['info']['townlabel'].setText("Town Name")
        self.widgets['info']['peoplelabel'].setText("Number of residents")
        self.widgets['info']['eventlabel'].setText("Number of Events")

        # staging area widget setup
        self.widgets['stage'].doubleClicked.connect(self.delsig)

        # file browser widget setup
        self.models['tree'].setRootPath('')
        self.widgets['tree'].setModel(self.models['tree'])
        self.widgets['tree'].setRootIndex(self.models['tree'].index('./data'))
        self.widgets['tree'].setAnimated(False)
        self.widgets['tree'].setIndentation(15)
        self.widgets['tree'].setSortingEnabled(True)
        self.widgets['tree'].hideColumn(1)
        self.widgets['tree'].hideColumn(2)
        self.widgets['tree'].hideColumn(3)
        self.widgets['tree'].doubleClicked.connect(self.addsig)

        # signals
        self.widgets['add'].clicked.connect(self.addsig)
        self.widgets['info']['build'].clicked.connect(self.buildsig)

        # add to grid layout
        self.layouts['main'].addWidget(self.widgets['tree'],0,0,1,3)
        self.layouts['main'].addWidget(self.widgets['new'],1,0)
        self.layouts['main'].addWidget(self.widgets['edit'],1,1)
        self.layouts['main'].addWidget(self.widgets['add'],1,2)
        self.layouts['main'].addWidget(self.widgets['stagebox'],0,3,2,1)
        self.layouts['main'].addWidget(self.widgets['info']['object'],0,4,2,1)

        self.layouts['towninfo'].addWidget(self.widgets['info']['townlabel'],0,0)
        self.layouts['towninfo'].addWidget(self.widgets['info']['towntext'],0,1)
        self.layouts['towninfo'].addWidget(self.widgets['info']['peoplelabel'],1,0)
        self.layouts['towninfo'].addWidget(self.widgets['info']['eventlabel'],2,0)
        self.layouts['towninfo'].addWidget(self.widgets['info']['build'],4,0,1,2)

        self.layouts['stage'].addWidget(self.widgets['stage'])

        # grid layout options
        self.layouts['main'].setColumnStretch(3,3)
        self.layouts['main'].setColumnStretch(4,4)
        self.layouts['towninfo'].setRowStretch(3,4)

    ### signals ###

    def addsig(self):
        # get file name from tree
        index = self.widgets['tree'].currentIndex()
        path = self.models['tree'].filePath(index)

        # adds the file(s) to the town to be written at the build stage
        self.recursive_add(path)

    def delsig(self):
        print('DELETE SIGNAL')
        # get file name
        pathkey = self.widgets['stage'].selectedIndexes()[0].data()

        # remove it
        path = self.town.getPath(pathkey)
        success = self.town.remove(pathkey)

        if success:
            self.setStatus('Removed: ' + path)
            self.log_change('remove', pathkey, path)

    def newsig(self):
        if self.town.active:
            reply = QMessageBox.question(self, 'Are you sure?', "Changes have been made. Continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No: return

        # clear
        self.town.clear()
        self.changes.clear()

        # reset stuff
        self.widgets['info']['towntext'].setText('')
        self.mvp.menu['&Edit']['&Undo'].setDisabled(True)
        self.mvp.menu['&Edit']['&Redo'].setDisabled(True)

        # new stuff and update
        self.town.new()
        self.status('New town loaded')
        self.update_staging()

    def loadsig(self):
        if self.town.active:
            reply = QMessageBox.question(self, 'Error', "A town is already loaded.  Do you want to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.town.clear()
                self.load_town()
        else:
            self.load_town()

    def buildsig(self):
        # get town name
        townname = self.widgets['info']['towntext'].text()

        # check if town loaded and name given
        if not self.town.active:
            print("placeholder to make python happy")
            self.setStatus('Nothing to save')
        elif townname == '':
            print("placeholder")
            self.setStatus('Need a town name to save')
        else:
            # save it
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', './towns')
            if filename != '':
                if filename[-5:] != '.json': filename = filename + '.json'
                success = self.town.build(townname, filename)
                if success: self.setStatus('Saved to ' + filename)
                else: self.setStatus('Something happened.')

    def undosig(self):
        # get change
        change = self.changes.undo()
        print(change)

        if change['action'] == 'add':
            self.town.remove(change['pathkey'])
        elif change['action'] == 'remove':
            self.town.add(change['path'])

        # notify user
        self.setStatus("Undo: add " + change['path'])

        # disability claims
        self.ViewMainMenu['&Edit']['&Redo']['disabled'] = "False"
        if self.changes.canUndo() == False:
            self.ViewMainMenu['&Edit']['&Undo']['disabled'] = "True"
        self.mvp.setmenu(self.getMenu())

        # update staging view
        self.update_staging()

    def redosig(self):
        # get change
        change = self.changes.redo()

        if change['action'] == 'add':
            self.town.add(change['path'])
        elif change['action'] == 'remove':
            self.town.remove(change['pathkey'])

        # disability claims
        self.mvp.menu['&Edit']['&Undo'].setDisabled(False)
        if not self.changes.canRedo(): self.mvp.menu['&Edit']['&Redo'].setDisabled(True)

        # update staging view
        self.update_staging()

    ## signal helpers

    def update_staging(self):
        self.widgets['stage'].clear()
        self.widgets['stage'].addItems(self.town.mods.keys())

    def load_town(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', './towns')
        if name:
            self.town.load(name)
            #self.status.showMessage("Town loaded")
            self.widgets['info']['towntext'].setText(self.town.data['name'])
        #else: self.status.showMessage("No town loaded")

    def recursive_add(self, path):
        # recursion
        if os.path.isdir(path):
            contents = glob.glob(path + '/*')
            for i in contents:
                self.recursive_add(i)
        else:
            pathkey = self.town.add(path)

            self.log_change('add', pathkey, path)

            if pathkey != '': self.setStatus('Added: ' + path)
            else: self.setStatus('Error: ' + fullname + ' is not valid')

    def log_change(self, action, pathkey, path):
        # log it
        self.changes.log({'action': action, 'path': path, 'pathkey': pathkey})

        # update gui
        self.ViewMainMenu['&Edit']['&Undo']['disabled'] = "False"
        if not self.changes.canRedo():
            self.ViewMainMenu['&Edit']['&Redo']['disabled'] = "True"
        self.mvp.setmenu(self.getMenu())
        #self.menu['edit_undo'].setDisabled(False)
        #if self.changes.canRedo() == False: self.menu['edit_redo'].setDisabled(True)
        self.update_staging()
