# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

import json
import glob

class Town:
    def __init__(self):
        self.data = {}
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

    def export(self, fn):
        with open(fn, 'w') as fp:
            json.dump(self.data, fp)
        self.active = False
    
    def clear(self):
        self.data.clear()
        self.active = False

    ## get functions

    # file grabbing
    def get_event_files(self):
        return glob.glob('data/event.*.json')

    def get_townspeople_files(self):
        return glob.glob('data/townspeople.*.json')

    # data grabbing
    def get_townspeople(self):
        return self.data['townspeople'].keys()

    # TESTING
    def dothing(self):
        event = json.load(open('data/event.dragonattack.json'))
        event2 = json.load(open('data/event.blizzard.json'))
        self.data['events'].update(event)
        self.data['events'].update(event2)
        tp = json.load(open('data/townspeople.common.json'))
        self.data['townspeople'].update(tp)

if __name__ == '__main__':
    # welcome message
    print("Town")

    # setup
    t = Town()
    t.clear()
