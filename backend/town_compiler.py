# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

import json

class TownCompiler:
    def __init__(self):
        self.data = {}

    def new_town(self, name):
        self.data['name'] = name
        self.data['characters'] = {}
        self.data['events'] = {}
    
    def load_town(self, fn):
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def export_town(self, fn):
        with open(fn, 'w') as fp:
            json.dump(self.data, fp)

# welcome message
print("Town Compiler")

# setup
tc = TownCompiler()

#tc.load_town('data/yeoldentowne.json')
tc.new_town('crap test town')
tc.export_town('crap.json')

# main loop
while True:
    print('What do?')
    i = input()
    if i is 'q': break
    print('')

