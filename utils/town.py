# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

# TODO: Add error checking
# TODO:

import os, glob, json

class Town:
    def __init__(self):
        self.data = {}
        self.mods = {}
        self.stats = {}
        self.active = False

    def new(self):
        self.data['people'] = {}
        self.data['events'] = {}

    def load(self, fn):
        self.active = True
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def clear(self):
        self.data.clear()
        self.mods.clear()
        self.active = False

    def add(self, path):
        # indicate changes have been made
        self.active = True

        # get current directory for string manipulation
        # TODO: error check for .json
        curr = os.path.dirname(os.path.abspath(__file__))

        # get partial but still unique path
        part = path[len(curr)+6:]

        # open file
        # TODO: error check this
        f = json.load(open(path))

        # add
        self.mods[part] = {}
        self.mods[part]['path'] = path
        self.mods[part]['data'] = f

        # TODO: actually error check
        return part

    def remove(self, path):
        change = self.mods.pop(path)

        # TODO: actually error check
        return True

    def getPath(self, pathkey):
        if pathkey in self.mods:
            return self.mods[pathkey]['path']
        else: return ''

    def build(self, tn, fn):
        if self.active:
            # make changes
            self.data['name'] = tn

            for i in self.mods:
                if 'people' in self.mods[i]['data']:
                    self.data['people'].update(self.mods[i]['data']['people'])
                if 'events' in self.mods[i]['data']:
                    self.data['events'].update(self.mods[i]['data']['events'])

            # write the file
            with open(fn, 'w') as fp:
                json.dump(self.data, fp)

            # reset
            self.active = False

            # return success
            return True
        else: return False

    ## get functions

    # data grabbing
    def get_people(self):
        return self.data['people'].keys()
