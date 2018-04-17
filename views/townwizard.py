# Town Wizard
# Purpose: A wizard (joke completely intended) to aid in the
#          compilation of town elements
# Author:  Ben Johnson


import os
import sys
import glob
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.town import Town
from utils.changes import Changes
from utils.multiview import View


class TownWizard(View):
    def setup_view(self):
        self.load_menu('config/wiz-menu.json')

        # variables
        self.widgets = {}
        self.layouts = {}
        self.town = Town()
        self.changes = Changes()
        self.stagelist = []

        # build interface
        self.setup_widgets()
        self.setup_layouts()
        self.build()

    def setup_widgets(self):
        # boxes
        self.widgets['seed-box'] = QGroupBox('Seed Generation')
        self.widgets['build-box'] = QGroupBox('Town Generation')

        # seed area
        self.widgets['tree'] = QTreeView()
        self.widgets['stage'] = QListWidget()
        self.widgets['gen-seed'] = QPushButton('Generate Seed')

        # build area
        self.widgets['load-seed'] = QPushButton('Load')
        self.widgets['seed-stats'] = QPushButton('Stats')
        self.widgets['load-text'] = QLineEdit()
        self.widgets['town-name'] = QLineEdit()
        self.widgets['town-pop'] = QLineEdit()
        self.widgets['town-years'] = QLineEdit()
        self.widgets['town-gen'] = QPushButton('Generate Town')

        # tree stuff
        self.treemodel = QFileSystemModel()
        self.treemodel.setRootPath('')
        self.widgets['tree'].setModel(self.treemodel)
        self.widgets['tree'].setRootIndex(self.treemodel.index('./data'))
        self.widgets['tree'].setAnimated(False)
        self.widgets['tree'].setIndentation(15)
        self.widgets['tree'].setSortingEnabled(True)
        self.widgets['tree'].hideColumn(1)
        self.widgets['tree'].hideColumn(2)
        self.widgets['tree'].hideColumn(3)

        # options
        self.widgets['tree'].setFixedWidth(200)
        self.widgets['stage'].setFixedWidth(200)
        self.widgets['seed-stats'].setDisabled(True)

        self.widgets['load-text'].setPlaceholderText('Seed')
        self.widgets['town-name'].setPlaceholderText('Town Name')
        self.widgets['town-pop'].setPlaceholderText('Population')
        self.widgets['town-years'].setPlaceholderText('Years of History')

        # signals
        self.widgets['gen-seed'].clicked.connect(self.seedgensig)
        self.widgets['tree'].doubleClicked.connect(self.seedaddsig)
        self.widgets['load-seed'].clicked.connect(self.seedloadsig)
        self.widgets['town-gen'].clicked.connect(self.towngensig)

    def setup_layouts(self):
        # initialize layouts
        self.layouts['seed'] = QGridLayout()
        self.layouts['build'] = QGridLayout()
        self.layouts['main'] = QGridLayout()

        # set layouts to widgets
        self.widgets['seed-box'].setLayout(self.layouts['seed'])
        self.widgets['build-box'].setLayout(self.layouts['build'])
        self.set_layout(self.layouts['main'])

    def build(self):
        # seed area
        self.layouts['seed'].addWidget(self.widgets['tree'], 0, 0, 3, 1)
        self.layouts['seed'].addWidget(QLabel('Staging area'), 0, 1)
        self.layouts['seed'].addWidget(self.widgets['stage'], 1, 1)
        self.layouts['seed'].addWidget(self.widgets['gen-seed'], 2, 1)

        # build area
        self.layouts['build'].addWidget(self.widgets['load-text'], 0, 0, 1, 2)
        self.layouts['build'].addWidget(self.widgets['load-seed'], 1, 0)
        self.layouts['build'].addWidget(self.widgets['seed-stats'], 1, 1)
        self.layouts['build'].addWidget(self.widgets['town-name'], 2, 0, 1, 2)
        self.layouts['build'].addWidget(self.widgets['town-pop'], 3, 0, 1, 2)
        self.layouts['build'].addWidget(self.widgets['town-years'], 4, 0, 1, 2)
        self.layouts['build'].addWidget(self.widgets['town-gen'], 6, 0, 1, 3)

        self.layouts['build'].setRowStretch(5, 4)

        # main widget
        self.layouts['main'].addWidget(self.widgets['seed-box'], 0, 0)
        self.layouts['main'].addWidget(self.widgets['build-box'], 0, 1)

    # ## seed signals ## #

    def seedgensig(self):
        self.seeddumpsig()

        # error checking
        if len(self.stagelist) == 0:
            self.set_status('Nothing to make a seed out of')
            return

        good = self.town.seed.check_integrity()

        if not good:
            self.set_status('Bad seed')
            return

        # get filename
        fn, _ = QFileDialog.getSaveFileName(self, 'Save File', './seeds')
        if fn != '':
            if fn[-5:] != '.json':
                fn = fn + '.json'

        # build seed
        self.town.seed_build(fn)

        # load the seed for town building
        self.town.seed_load(fn)
        self.widgets['load-text'].setText(fn)

    def seeddumpsig(self):
        print('occupations:')
        for i in self.town.seed.occupations:
            print('  ' + i)
        print('male names:')
        for i in self.town.seed.names['male']:
            print('  ' + i)
        print('female names:')
        for i in self.town.seed.names['female']:
            print('  ' + i)
        print('last names:')
        for i in self.town.seed.names['last']:
            print('  ' + i)

    def seedloadsig(self):
        print('load seed')
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', './seeds')

        # error check
        if name != '':
            self.town.seed_load(name)
            self.widgets['load-text'].setText(name)
            self.set_status(f'Seed {name} loaded')

    def seedaddsig(self):
        # get file name from tree
        index = self.widgets['tree'].currentIndex()
        path = self.treemodel.filePath(index)

        # adds the file(s) to the town to be written at the build stage
        self.recursive_add(path)

    # ## build signals ## #

    def towngensig(self):
        # variables
        tname = self.widgets['town-name'].text()
        pop = self.widgets['town-pop'].text()
        years = self.widgets['town-years'].text()

        # error checking
        if not self.town.active:
            self.set_status('No seed loaded')
            return
        if tname == '':
            self.set_status('No town name given')
            return
        if pop == '':
            self.set_status('No population given')
            return
        if years == '':
            self.set_status('No years given')
            return

        fname, _ = QFileDialog.getSaveFileName(self, 'Save File', './towns')

        if fname != '':
            self.town.gen_town(int(pop), int(years), tname, fname)

    # ## signals ## #

    def spitsig(self):
        self.town.spit()

    def delsig(self):
        print('DELETE SIGNAL')
        # get file name
        pathkey = self.widgets['stage'].selectedIndexes()[0].data()

        # remove it
        path = self.town.getPath(pathkey)
        success = self.town.remove(pathkey)

        if success:
            self.set_status('Removed: ' + path)
            self.log_change('remove', pathkey, path)

    def newsig(self):
        if self.town.active:
            reply = QMessageBox.question(self,
                                         'Are you sure?',
                                         "Changes have been made. Continue?",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.No:
                return

        # clear
        self.town.clear()
        self.changes.clear()

        # reset stuff
        self.widgets['info-towntext'].setText('')
        self.widgets['info-poptext'].setText('')
        self.parent.menu['&Edit']['&Undo'].setDisabled(True)
        self.parent.menu['&Edit']['&Redo'].setDisabled(True)

        # new stuff and update
        self.town.new()
        self.set_status('New town loaded')
        self.update_staging()

    def buildsig(self):
        # get town name
        townname = self.widgets['info-towntext'].text()
        townpop = self.widgets['info-poptext'].text()

        # check if town loaded and name given
        if not self.town.active:
            self.set_status('Nothing to save')
        elif townname == '':
            self.set_status('Need a town name to save')
        elif townpop == '':
            self.set_status('Need a population.  No ghost towns allowed')
        else:
            # save it
            filename, _ = QFileDialog.getSaveFileName(self,
                                                      'Save File', './towns')
            if filename != '':
                if filename[-5:] != '.json':
                    filename = filename + '.json'
                success = self.town.build(filename, townname, townpop)
                if success:
                    self.set_status('Saved to ' + filename)
                else:
                    self.set_status('Something happened.')

    def undosig(self):
        # get change
        change = self.changes.undo()

        # error checking
        if change is None:
            return

        if change['action'] == 'add':
            self.town.remove(change['pathkey'])
        elif change['action'] == 'remove':
            self.town.seed_add(change['path'])

        # notify user
        self.set_status("Undo: add " + change['path'])

        # disability claims
        self.get_menu()['&Edit']['&Redo']['disabled'] = "False"
        if self.changes.canUndo() is False:
            self.get_menu()['&Edit']['&Undo']['disabled'] = "True"
        self.update_menu()

        # update staging view
        self.update_staging()

    def redosig(self):
        print('REDO SIGNAL')
        # get change
        change = self.changes.redo()

        # error checking
        if change is None:
            return

        if change['action'] == 'add':
            self.town.seed_add(change['path'])
        elif change['action'] == 'remove':
            self.town.remove(change['pathkey'])

        # disability claims
        self.get_menu()['&Edit']['&Undo']['disabled'] = "False"
        if not self.changes.canRedo():
            self.parent.menu['&Edit']['&Redo'].setDisabled(True)

        # update staging view
        self.update_staging()

    # signal helpers

    def update_staging(self):
        self.widgets['stage'].clear()
        self.widgets['stage'].addItems(self.stagelist)

    def load_town(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', './towns')
        if name:
            self.town.load(name)
            self.set_status("Town loaded")
            self.widgets['info-towntext'].setText(self.town.data['name'])
            self.widgets['info-poptext'].\
                setText(str(self.town.data['population']))
        else:
            self.set_status("No town loaded")

    def recursive_add(self, path):
        # recursion
        if os.path.isdir(path):
            contents = glob.glob(path + '/*')
            for i in contents:
                self.recursive_add(i)
        else:
            pathkey = self.town.seed_add(path)
            print(f'got pathkey: {pathkey}')

            if pathkey != '':
                self.set_status('Added: ' + path)
                self.stagelist.append(pathkey)
                self.log_change('add', pathkey, path)
            else:
                self.set_status('Error: ' + fullname + ' is not valid')

    def log_change(self, action, pathkey, path):
        '''
        # log it
        self.changes.log({'action': action, 'path': path, 'pathkey': pathkey})

        # update gui
        self.get_menu()['&Edit']['&Undo']['disabled'] = "False"
        if not self.changes.canRedo():
            self.get_menu()['&Edit']['&Redo']['disabled'] = "True"

        # update
        self.update_menu()
        self.update_staging()
        '''

        print('logging change (lol not really)')
        self.update_staging()
