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

        """ Set up fillers."""
        topFill = QWidget()
        topFill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottomFill = QWidget()
        bottomFill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        wizardButton = self.createWizardButton(mainWidget)
        closeButton = self.createCloseButton(mainWidget)

        layout = QVBoxLayout()
        layout.setContentsMargins(100, 0, 100, 0)
        layout.addWidget(topFill)
        layout.addWidget(wizardButton)
        layout.addWidget(closeButton)
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
        box.exec_()

    def createActions(self):
        """Create actions that go inside of main toolbar options."""
        self.exitAct = QAction("&Exit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application",
                               triggered=self.close)

        self.aboutAct = QAction("&About", self, statusTip="Show the about box",
                                triggered=self.about, shortcut="Ctrl+A")

    def createMenus(self):
        """Generate Menubar and populate."""
        self.mainMenuBar = self.menuBar()
        self.mainMenuBar.setNativeMenuBar(False)
        self.fileMenu = self.mainMenuBar.addMenu("&File")
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addAction(self.aboutAct)

        self.editMenu = self.menuBar().addMenu("&Edit")

    def createWizardButton(self, widget):
        """Create buttons for menu."""
        self.wizardButton = QPushButton("Wizard", widget)
        self.wizardButton.clicked.connect(self.showWizard)
        return self.wizardButton

    def createCloseButton(self, widget):
        """Create close button."""
        self.closeButton = QPushButton("Close", widget)
        self.closeButton.clicked.connect(self.close)
        return self.closeButton

    def showWizard(self):
        """Change window to wizard."""
        print("Showing wizard here")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
