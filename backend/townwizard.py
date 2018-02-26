# Town Wizard
# Purpose: A wizard (pun completely intended) to aid in the
#          compilation of town elements
# Author:  Ben Johnson

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from town_compiler import TownCompiler

import sys

class CreatorWin(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'D&D Town Creator'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # add elements and setup layout
        self.setup()
        
        # show the window
        self.show()
   
    def setup(self):
        # views
        self.mainview = QGroupBox("Create yo")
        gridlayout = QGridLayout()
        
        # widgets
        self.tree = QTreeView()
        
        # file browser widget setup
        self.treebase = QFileSystemModel()
        self.treebase.setRootPath('')
        self.tree.setModel(self.treebase)
        self.tree.setRootIndex(self.treebase.index('./data'))
        self.tree.setAnimated(False)
        self.tree.setIndentation(15)
        self.tree.setSortingEnabled(True)
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
 
        # Editor

        # add to grid layout
        gridlayout.setColumnStretch(2, 4)
        gridlayout.setColumnStretch(3, 4)
        gridlayout.addWidget(self.tree,0,0,1,2)
        gridlayout.addWidget(QPushButton('2'),0,2)
        gridlayout.addWidget(QPushButton('2'),0,3)
        gridlayout.addWidget(QPushButton('New'),1,0)
        gridlayout.addWidget(QPushButton('Edit'),1,1)
        
        # set layout
        self.setLayout(gridlayout)


if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)
    
    # initalize classes
    tc = TownCompiler()
    win = CreatorWin()
    
    # setup
    tc.load_town('towns/comptest.json')
    
    # clean up and exit
    sys.exit(app.exec_())



    '''
    listWidget = QListWidget()

    listWidget.addItems(tc.get_event_files())
    listWidget.show()
    '''


