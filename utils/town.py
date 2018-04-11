# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

# TODO: Add error checking
# TODO:


import os
import glob
import json


class TownSeed:
    def __init__(self):
        self.people = {}
        self.events = {}


class Town:
    def __init__(self):
        self.data = {}
        self.active = False

        # start new TownSeed class
        self.seed = TownSeed()

        # set blanks
        self.data['name'] = ''
        self.data['population'] = ''
        self.data['occupations'] = {}
        self.data['events'] = {}

    # ## seed ## #

    def seed_load(self, fn):
        # setup and reset
        self.active = True
        self.seed.people.clear()
        self.seed.events.clear()

        # open file
        with open(fn, 'r') as f:
            data = json.load(f)

        # integrity check
        if data['type'] != 'Seed':
            return

        # load people
        for i in data['people']:
            self.seed.people[i] = data['people'][i]

        # load events
        for i in data['events']:
            self.seed.events[i] = data['events'][i]

    def seed_add(self, path):
        # indicate changes have been made
        self.active = True

        # get current directory for string manipulation
        # TODO: error check for .json
        curr = os.path.dirname(os.path.abspath(__file__))
        print(curr)
        # get partial but still unique path
        part = path[len(curr)+6:]

        # open file
        # TODO: error check this
        f = json.load(open(path))

        # TODO: integrity check the file

        # check type
        if f['type'] == 'Person':
            self.seed.people[f['title']] = f
        elif f['type'] == 'Event':
            self.seed.events[f['title']] = f
        else:
            return ''

        # TODO: actually error check
        print(part)
        return part

    def seed_remove(self, name):
        pass

    def seed_build(self, fn):
        wdata = {}

        # header
        wdata['type'] = 'Seed'
        wdata['people'] = {}
        wdata['events'] = {}

        # insert data
        for i in self.seed.people:
            wdata['people'][i] = self.seed.people[i]
        for i in self.seed.events:
            wdata['events'][i] = self.seed.events[i]

        with open(fn, 'w') as f:
            json.dump(wdata, f)

    # ## town ## #

    def gen_town(self, num_people, num_years):
        pass

    def new(self):
        self.data['name'] = ''
        self.data['occupations'] = {}
        self.data['events'] = {}

    def load(self, fn):
        self.active = True
        with open(fn, 'r') as fp:
            self.data = json.load(fp)

    def clear(self):
        self.data.clear()
        self.mods.clear()
        self.active = False

    def remove(self, path):
        change = self.mods.pop(path)

        # TODO: actually error check
        return True

    def getPath(self, pathkey):
        if pathkey in self.mods:
            return self.mods[pathkey]['path']
        else:
            return ''

    def build(self, fn, tn, pop):
        if self.active:
            # make changes
            self.data['name'] = tn
            self.data['population'] = int(pop)

            for i in self.mods:
                if 'occupations' in self.mods[i]['data']:
                    self.data['occupations'].\
                        update(self.mods[i]['data']['occupations'])
                if 'events' in self.mods[i]['data']:
                    self.data['events'].update(self.mods[i]['data']['events'])

            # write the file
            with open(fn, 'w') as fp:
                json.dump(self.data, fp)

            # return success
            return True
        else:
            return False

    # get functions #

    # data grabbing
    def get_people(self):
        return self.data['people'].keys()

    # HWAPATEWEE
    def spit(self):
        if not self.active:
            return
        print('Name: ' + self.data['name'])
        print('Population: ' + str(self.data['population']))
        print('Occupations:')
        for i in self.data['occupations']:
            print('  ' + i)
        print('Events:')
        for i in self.data['events']:
            print('  ' + i + ': ' + self.data['events'][i]['description'])
            print('  Outcomes:')
            for j in self.data['events'][i]['outcomes']:
                desc = self.data['events'][i]['outcomes'][j]['description']
                print(f'    {j}: {desc}')
