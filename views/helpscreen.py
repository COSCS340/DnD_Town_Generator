from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from utils.multiview import View


class HelpMenu(View):
    def setup_view(self):
        self.load_menu('config/help-menu.json')

        self.widgets = {}
        self.layouts = {}
        self.setupInterface()

    def setupInterface(self):
        self.layouts['main'] = QGridLayout()

        self.widgets['label'] = QLabel("help screen")
        self.layouts['main'].addWidget(self.widgets['label'])

        self.set_layout(self.layouts['main'])

    def sig(self):
        sys.exit()
