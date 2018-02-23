from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar
from PyQt5 import QtGui
import sys

class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #OSX toolbar
        if sys.platform == 'darwin':
            print("You're running mac")
            from PyQt5.QtMacExtras import QMacToolBar
            sys.exit()

        else:
            print("You're runing not-mac")
            self.toolbar = self.addToolBar('Bar')

        #exitButton = QtWidgets.QAction(QtGui.QIcon('exit.png'), ' &Exit', self)
        fileButton = QtWidgets.QAction("File", self)
        fileButton.setShortcut('Ctrl+Q')
        fileButton.setStatusTip('Exit application')
        fileButton.triggered.connect(self.close)

        self.toolbar.addAction(fileButton)
        self.toolbar.setMovable(False)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu")

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
