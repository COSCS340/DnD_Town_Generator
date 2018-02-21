from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
import sys

class Thing(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('OK', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(415, 515)

        self.setGeometry(425, 100, 500, 550)
        self.setWindowTitle('Help')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Thing()
    sys.exit(app.exec_())
