# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

# TODO: Add error checking
# TODO:


import os
import glob
import json

from utils.person import Person


class TownSeed:
    def __init__(self):
        self.people = []
        self.events = {}
        self.names = {}
        self.active = False

        # names structure
        self.names['first'] = []
        self.names['last'] = []

    def check_integrity(self):
        if len(self.names['first']) == 0:
            return False
        elif len(self.people) == 0:
            return False
        else:
            return True


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

        # load things
        self.seed.people = data['people']
        self.seed.events = data['events']
        self.seed.names = data['names']

        # check integrity
        good = self.seed.check_integrity()
        if not good: return

    def seed_add(self, path):
        # indicate changes have been made
        self.active = True

        # get current directory for string manipulation
        # FIXME: this does not work
        curr = os.path.dirname(os.path.abspath(__file__))
        print(curr)

        # get partial but still unique path
        part = path.split('data')[1]  # path[len(curr)+6:]

        # open file
        # TODO: error check this
        f = json.load(open(path))

        # TODO: integrity check the file

        # check type
        if f['type'] == 'Person':
            self.seed.people[f['title']] = f
        elif f['type'] == 'Event':
            self.seed.events[f['title']] = f
        elif f['type'] == 'Names':
            # merge new names into existing names
            # TODO: remove duplicates
            self.seed.names['first'].append(f['first'])
            self.seed.names['last'].append(f['last'])
        else:
            return ''

        # TODO: actually error check
        print(part)
        return part

    def seed_remove(self, name):
        pass

    def seed_build(self, fn):
        wdata = {}

        # check integrity
        good = self.seed.check_integrity()
        if not good: return

        # header
        wdata['type'] = 'Seed'
        wdata['people'] = {}
        wdata['events'] = {}
        wdata['names'] = {}

        # insert data
        wdata['people'] = self.seed.people
        wdata['events'] = self.seed.events
        wdata['names'] = self.seed.names

        with open(fn, 'w') as f:
            json.dump(wdata, f)

    # ## town ## #

    def name_people(self, num_people):
        for i in range(0, num_people):
            tmp = Person()
            # TODO: do yo thing on each person
            # 2 random numbers
            # grab from first and last
            # add names to tmp
            # append (which is below)

            # names are given in self.seed.names['first'/'last']

            self.people.append(Person())


    def gen_town(self, num_people, num_years):
        self.name_people(num_people)

        for i in range(0, num_years): #loop on number of years
            for j in range(0, num_people):
                r = randint(0, 4)
                if r == 4:
                    r = randint(0,9)
                    if r < 6:
                        print('Giving an event 1')#pick an event
                    elif r < 9:
                        print('Giving an event 2')#pick a 2
                    else:
                        print('Giving an event 3')#pick a 3

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
