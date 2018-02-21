from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtWidgets.qApp.quit())

        self.statusBar()

        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu")
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
