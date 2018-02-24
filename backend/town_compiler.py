# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

import json

class TownCompiler:
    def __init__(self):
        self.data = {}

    def new_town(self, name):
        self.data['name'] = name
        self.data['townspeople'] = {}
        self.data['events'] = {}
    
    def load_town(self, fn):
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def export_town(self, fn):
        with open(fn, 'w') as fp:
            json.dump(self.data, fp)

    def get_townspeople(self):
        return self.data['characters'].keys()

    def dothing(self):
        event = json.load(open('data/event.dragonattack.json'))
        event2 = json.load(open('data/event.blizzard.json'))
        self.data['events'].update(event)
        self.data['events'].update(event2)

if __name__ == '__main__':
    # welcome message
    print("Town Compiler")

    # setup
    tc = TownCompiler()

    tc.load_town('data/crap.json')
    tc.dothing()
    tc.export_town('data/crap2.json')

    '''
    # main loop
    while True:
        print('What do?')
        i = input()
        if i is 'q': break
        print('')
    '''
