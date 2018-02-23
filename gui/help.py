from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

#path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'help.ico')

class Thing(QWidget):

    def __init__(self):
        super().__init__()
        #self.setWindowIcon(QtGui.QIcon('help1.png'))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        print (scriptDir + os.path.sep + "help.ico")
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'help.ico'))
        #self.setWindowIcon(QtGui.QIcon(path))
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('OK', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(415, 515)

        self.setGeometry(425, 100, 500, 550)
        self.setWindowTitle('Help')

        #scriptDir = os.path.dirname(os.path.realpath(__file__))
        #print (scriptDir + os.path.sep + "help1.png")
        #self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'help1.png'))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Thing()
    sys.exit(app.exec_())
