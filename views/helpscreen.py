from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import QFile, QTextStream
from os import getcwd
from utils.multiview import View

class HelpMenu(View):
    def setup_view(self):
        self.load_menu('config/help-menu.json')

        self.widgets = {}
        self.layouts = {}
        self.setupInterface()

    def setupInterface(self):
        self.layouts['main'] = QVBoxLayout()

        path = str(getcwd()) + '/views/html/help.html'
        file = QFile(path)
        results = file.open(QFile.ReadOnly|QFile.Text)
        istream = QTextStream(file)

        self.widgets['test'] = QTextEdit()
        self.widgets['test'].setReadOnly(True)
        self.widgets['test'].setHtml(istream.readAll())
        file.close()

        '''
        self.widgets['test'] = QTextEdit("Welcome to our town generator!</br> "
                                        "When you click the 'wizard' tab, ")
        self.widgets['test'].setReadOnly(True)
        self.widgets['wizard'] = QLabel("When you click the 'wizard' tab, "
                                        "you'll see a page that allows seeds "
                                        "for towns to be generated!")
        self.widgets['load'] = QLabel("To load a town, click 'Load' on the "
                                        "right side of the page. ")
        self.widgets['gen'] = QLabel("")
        '''

        self.layouts['main'].addWidget(self.widgets['test'])
        # self.layouts['main'].addWidget(self.widgets['wizard'])
        # self.layouts['main'].addWidget(self.widgets['load'])

        self.set_layout(self.layouts['main'])

    def sig(self):
        sys.exit()
