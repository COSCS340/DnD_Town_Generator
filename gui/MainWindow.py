from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar
from PyQt5 import QtGui
import sys

class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.toolbar = self.addToolBar('Bar')

        #exitButton = QtWidgets.QAction(QtGui.QIcon('./exit.png'), ' &Exit', self)
        exitButton = QtWidgets.QAction("File", self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        self.toolbar.addAction(exitButton)
        self.toolbar.setMovable(False)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu")

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
