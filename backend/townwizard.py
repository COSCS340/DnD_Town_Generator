# Town Wizard
# Purpose: A wizard (joke completely intended) to aid in the
#          compilation of town elements
# Author:  Ben Johnson


import os, sys, glob
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from town import Town


class Wizard(QtWidgets.QMainWindow):
    def __init__(self):
        # variables
        super().__init__()
        self.title = 'D&D Town Wizard'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.town = Town()

        # init
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # variables
        self.models = {}
        self.widgets = {}
        
        # add elements and setup layout
        self.setupInterface()
        self.setupMenu()
        
        # show the window
        self.show()

    def setupInterface(self):
        # layout
        gridlayout = QGridLayout()
        
        # widgets
        self.widgets['tree'] = QTreeView()
        self.widgets['selected'] = QListWidget()
        self.widgets['new'] = QPushButton('New')
        self.widgets['edit'] = QPushButton('Edit')
        self.widgets['add'] = QPushButton('Add')
        self.widgets['build'] = QPushButton('Build Town')
        self.widgets['newtown'] = QPushButton('New Town')
        self.widgets['loadtown'] = QPushButton('Load Town')
        self.widgets['townlabel'] = QLabel(self)
        self.widgets['info'] = {}
        self.widgets['info']['townname'] = "New Town"

        # models
        self.models['tree'] = QFileSystemModel()

        # town name label widget setup
        self.widgets['townlabel'].setText("WHEE THIS IS SOME TEXT")
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
        self.widgets['tree'].doubleClicked.connect(self.filesig)
        
        # signals
        self.widgets['add'].clicked.connect(self.filesig)
        self.widgets['newtown'].clicked.connect(self.newsig)
        self.widgets['loadtown'].clicked.connect(self.loadsig)
        self.widgets['build'].clicked.connect(self.buildsig)

        # add to grid layout
        gridlayout.addWidget(self.widgets['tree'],0,0,1,3)
        gridlayout.addWidget(self.widgets['new'],1,0)
        gridlayout.addWidget(self.widgets['edit'],1,1)
        gridlayout.addWidget(self.widgets['add'],1,2)
        gridlayout.addWidget(self.widgets['selected'],0,3)
        gridlayout.addWidget(self.widgets['build'],1,3)
        #gridlayout.addWidget(self.widgets['townlabel'],0,5)
        gridlayout.setColumnStretch(3, 4)
        #gridlayout.setColumnStretch(4, 4)
        
        # set layout
        #self.setLayout(gridlayout)
        
        cw = QWidget(self)
        self.setCentralWidget(cw)
        cw.setLayout(gridlayout)

    def setupMenu(self):
        self.topbar = self.menuBar()
        self.status = self.statusBar()
        
        # status bar
        self.status.showMessage("Welcome. Load a town or start fresh.")
        
        # file menu
        file_menu = self.topbar.addMenu('File')
        file_open = QtWidgets.QAction('Open', self)
        file_new = QtWidgets.QAction('New', self)
        file_close = QtWidgets.QAction('Close', self)
        file_build = QtWidgets.QAction('Build', self)
        file_menu.addAction(file_open)
        file_menu.addAction(file_new)
        file_menu.addSeparator()
        file_menu.addAction(file_build)
        file_menu.addSeparator()
        file_menu.addAction(file_close)
        
        file_open.triggered.connect(self.loadsig)
        file_new.triggered.connect(self.newsig)
        file_build.triggered.connect(self.buildsig)
        
        # edit menu
        edit_menu = self.topbar.addMenu('Edit')
        
        # about menu
        about_menu = self.topbar.addMenu('Help')

    ## signals
    
    def filesig(self):
        # get file name
        index = self.widgets['tree'].currentIndex()
        fullname = self.models['tree'].filePath(index)
        
        # adds the files to the town to be written at the build stage
        self.add_file(fullname)

        # update
        self.widgets['selected'].clear()
        self.widgets['selected'].addItems(self.town.events.keys() | self.town.townspeople.keys())
    
    def newsig(self):
        if self.town.active:
            reply = QMessageBox.question(self, 'Error', "A town is already loaded.  Do you want to start over?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.town.clear()
                self.new_town()
        else:
            self.new_town()

    def loadsig(self):
        if self.town.active:
            reply = QMessageBox.question(self, 'Error', "A town is already loaded.  Do you want to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.town.clear()
                self.load_town()
        else:
            self.load_town()
    
    def buildsig(self):
        if self.town.active:
            name, _ = QFileDialog.getSaveFileName(self, 'Save File', './towns')

            if name != '':
                print(name[-5:])
                if name[-5:] != '.json': name = name + '.json'
                self.town.build(name)

    ## signal helpers

    def add_file(self, fullname):
        # get partial file name and type
        prettyname = fullname[(fullname.rfind('/') + 1):]
        ftype = prettyname[:prettyname.find('.')]

        # folder (recursive)
        if os.path.isdir(fullname):
            contents = glob.glob(fullname + '/*')
            for i in contents: 
                self.add_file(i)
        # event
        elif ftype == 'event':
            # if not already selected
            if prettyname not in self.town.events:
                self.town.events[prettyname] = fullname
                print(prettyname)
        # townspeople  
        elif ftype == 'townspeople':
            if prettyname not in self.town.townspeople:
                self.town.townspeople[prettyname] = fullname
                print(prettyname)
        else: self.status.showMessage("Not a valid file")

    def new_town(self):
        name, ok = QInputDialog.getText(self, "New Town","Town Name", QLineEdit.Normal, "")
        if ok:
            if name != '':
                self.town.new(name)
            else: QMessageBox.warning(self, "Name Error", "You did not enter a name. No town was created", QMessageBox.Ok, QMessageBox.NoButton)

    def load_town(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', './towns')
        if name:
            self.town.load(name)
            self.status.showMessage("Town loaded")
        else: self.status.showMessage("No town loaded")

if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)
    
    # initalize classes
    win = Wizard()

    # execute, clean up, and exit
    sys.exit(app.exec_())
