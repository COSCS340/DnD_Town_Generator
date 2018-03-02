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

    def new(self, name):
        self.active = True
        self.data['name'] = name
        self.data['people'] = {}
        self.data['events'] = {}
    
    def load(self, fn):
        self.active = True
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def clear(self):
        self.data.clear()
        self.events.clear()
        self.people.clear()
        self.active = False

    def add(self, path):
        # get partial name
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
        self.mods.pop(path)

        # TODO: actually error check
        return True

    def build(self, fn):
        for i in self.mods:
            self.data.update(self.mods[i]['data'])

        with open(fn, 'w') as fp:
            json.dump(self.data, fp)

        # reset
        self.active = False

    ## get functions

    # file grabbing
    def get_event_files(self):
        return glob.glob('data/event.*.json')

    def get_people_files(self):
        return glob.glob('data/people.*.json')

    # data grabbing
    def get_people(self):
        return self.data['people'].keys()
