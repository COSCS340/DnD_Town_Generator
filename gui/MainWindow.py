from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #OSX toolbar
        if sys.platform == 'darwin':
            from PyQt5.QtMacExtras import QMacToolBar

            #FIXME
            self.toolbar = self.addToolBar('Bar')
            self.toolbar.toggleViewAction()

        else:
            self.toolbar = self.addToolBar('Bar')
            self.toolbar.toggleViewAction()

        #exitButton = QAction(QtGui.QIcon('exit.png'), ' &Exit', self)
        fileButton = QAction("File", self)
        fileButton.setShortcut('Ctrl+Q')
        fileButton.setStatusTip('Exit application')
        fileButton.triggered.connect(self.close)

        self.toolbar.addAction(fileButton)
        self.toolbar.setMovable(False)

        wizardButton = QPushButton("Wizard", self)
        wizardButton.clicked.connect(self.showWizard)
        wizardButton.move(0,30)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu")
        self.setMinimumHeight(100)
        self.setMinimumWidth(100)

        self.show()

    def showWizard(self):
        print("Showing wizard here")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
