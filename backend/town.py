# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

# TODO: Add error checking

import json
import glob

class Town:
    def __init__(self):
        self.data = {}
        self.events = {}
        self.townspeople = {}
        self.active = False

    def new(self, name):
        self.active = True
        self.data['name'] = name
        self.data['townspeople'] = {}
        self.data['events'] = {}
    
    def load(self, fn):
        self.active = True
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def build(self, fn):
        for i in self.events:
            self.add_event_file(self.events[i])
        for i in self.townspeople:
            self.add_townspeople_file(self.townspeople[i])
        with open(fn, 'w') as fp:
            json.dump(self.data, fp)
        self.active = False
    
    def clear(self):
        self.data.clear()
        self.active = False

    def add_event_file(self, fn):
        event = json.load(open(fn))
        self.data['events'].update(event)

    def add_townspeople_file(self, fn):
        tp = json.load(open(fn))
        self.data['townspeople'].update(tp)

    ## get functions

    # file grabbing
    def get_event_files(self):
        return glob.glob('data/event.*.json')

    def get_townspeople_files(self):
        return glob.glob('data/townspeople.*.json')

    # data grabbing
    def get_townspeople(self):
        return self.data['townspeople'].keys()
