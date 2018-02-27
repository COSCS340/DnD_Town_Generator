# This is an intial working version of the main menu for our DND Generator.
# This will be worked on by Cody and Matt

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class Example(QtWidgets.QWidget):

    #call constructor for this class and parent QWidget class.
    def __init__(self):
        super().__init__()

        #Run gui initialize function
        self.initUI()

    #initialize gui
    def initUI(self):
        #Resize to box
        self.resize(100, 300)
        #Move position on screen
        self.Center()
        self.setWindowTitle('Menu')

        #initialize button, set to exit on press
        quit = QtWidgets.QPushButton('Quit', self)
        quit.clicked.connect(QtWidgets.QApplication.instance().quit) #FIXME need to set up warning
        quit.resize(quit.sizeHint())
        quit.move(0, 150)

        self.show()

    #Center the frame
    def Center(self):
        #get rectangle of frame
        geo = self.frameGeometry()
        #get resolution and then center
        cent = QtWidgets.QDesktopWidget().availableGeometry().center()
        #set center of frame to center of screen
        geo.moveCenter(cent)
        #move frame's top left to meet the geometry of window
        self.move(geo.topLeft())

    def closeEvent(self, event):
        response = QtWidgets.QMessageBox.question(self, 'Warning',
        'Are you sure you want to quit?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
         QtWidgets.QMessageBox.No)

        if response == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    #Initialize application
    app = QtWidgets.QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
