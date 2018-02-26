# Town Wizard
# Purpose: A wizard (pun completely intended) to aid in the
#          compilation of town elements
# Author:  Ben Johnson

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from town import Town

import sys


class CreatorWin(QWidget):
    def __init__(self):
        # variables
        super().__init__()
        self.title = 'D&D Town Creator'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.town = TownCompiler()

        # passed town
        #self.town = town
        
        # init
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # variables
        self.curr_list = []
        self.curr_file = ''
        
        # FOR NOW MAKES NEW TOWNS ONLY
        # self.town.new_town()

        # add elements and setup layout
        self.setup()
        
        # show the window
        self.show()

    def setup(self):
        # layout
        gridlayout = QGridLayout()
        
        # widgets
        self.tree = QTreeView()
        self.selected = QListWidget()
        self.new_file = QPushButton('New')
        self.edit_file = QPushButton('Edit')
        self.add_file = QPushButton('Add')
        self.compile = QPushButton('Create Town')
        
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
        self.tree.doubleClicked.connect(self.filesig)
        
        # add button widget setup
        self.add_file.clicked.connect(self.filesig)
 
        # Current element list
        self.selected.addItems(self.curr_list)

        # add to grid layout
        gridlayout.addWidget(self.tree,0,0,1,3)
        gridlayout.addWidget(self.new_file,1,0)
        gridlayout.addWidget(self.edit_file,1,1)
        gridlayout.addWidget(self.add_file,1,2)
        gridlayout.addWidget(self.selected,0,3)
        gridlayout.addWidget(self.compile,1,3)
        
        # set layout
        self.setLayout(gridlayout)

    # signals
    def filesig(self):
        index = self.tree.currentIndex()
        self.curr_file = self.treebase.filePath(index)
        self.curr_list.append(self.curr_file)
        print(self.curr_list)
   

if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)
    
    # initalize classes
    #tc = TownCompiler()
    win = CreatorWin()
    
    # setup
    
    
    # clean up and exit
    app.exec_()
    
    win.curr_list = tc.get_event_files()
    
    sys.exit()



    '''
    listWidget = QListWidget()

    listWidget.addItems(tc.get_event_files())
    listWidget.show()
    '''


