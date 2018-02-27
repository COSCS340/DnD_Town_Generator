"""
This is the official main menu for our application.

This is currently being worked on by Dakota Sanders.
"""

from PyQt5.QtWidgets import (QMainWindow, QAction, QPushButton, QApplication,
                             QMessageBox, QVBoxLayout, QWidget, QSizePolicy)
import sys


class Example(QMainWindow):
    """Menu class."""

    def __init__(self):
        """Basic constructor."""
        super().__init__()
        self.initUI()

    def initUI(self):
        """Set up menu."""
        ''' OSX toolbar
        this doesn't work ):
        if sys.platform == 'darwin':
            from PyQt5.QtMacExtras import QMacToolBar, QMacToolBarItem
            mac = True
            self.toolbar = self.addToolBar('Bar')
            self.toolbar.toggleViewAction()
            self.macFileButton = QMacToolBarItem()
            self.toolbar = QMacToolBar()
            self.toolbar.addItem(QIcon('exit.png'), "File")
            self.toolbar.attachToWindow(self.createWindowContainer(id))

        else:
            mac = False
        '''

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        self.createActions()
        self.createMenus()

        wizardButton = QPushButton("Wizard", mainWidget)
        wizardButton.clicked.connect(self.showWizard)
        wizardButton.move(0, 30)

        topFill = QWidget()
        topFill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        bottomFill = QWidget()
        bottomFill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(topFill)
        layout.addWidget(wizardButton)
        layout.addWidget(bottomFill)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Menu")
        self.setMinimumHeight(100)
        self.setMinimumWidth(100)
        mainWidget.setLayout(layout)

        self.show()

    def about(self):
        """About menu."""
        box = QMessageBox(self)
        box.setText("About goes here")

    def createActions(self):
        """Create actions that go inside of main toolbar options."""
        self.exitAct = QAction("&Exit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application",
                               triggered=self.close)

        self.aboutAct = QAction("&About", self, statusTip="Show the about box",
                                triggered=self.about)

    def createMenus(self):
        """Generate Menubar and populate."""
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addAction(self.aboutAct)

        self.editMenu = self.menuBar().addMenu("&Edit")

    def showWizard(self):
        """Change window to wizard."""
        print("Showing wizard here")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
