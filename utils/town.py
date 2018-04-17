# Town Compiler
# Author:  Ben Johnson
# Purpose: Compiles and/or edits a town

# TODO: Add error checking
# TODO:


import os
import glob
import json
from random import randint  # lolz so random xD

from utils.person import Person


class TownSeed:
    def __init__(self):
        self.occupations = {}
        self.events = {}
        self.names = {}
        self.active = False

        # names structure
        self.names['male'] = []
        self.names['female'] = []
        self.names['last'] = []

    def check_integrity(self):
        if len(self.names['male']) == 0:
            return False
        if len(self.names['female']) == 0:
            return False
        if len(self.names['last']) == 0:
            return False
        if len(self.occupations) == 0:
            return False
        return True


class Town:
    def __init__(self):
        self.active = False

        # start new TownSeed class
        self.seed = TownSeed()

        self.data = None

        self.name = ''
        self.population = 0
        self.citizens = []
        self.events = {}

    # ## seed ## #

    def seed_load(self, fn):
        # setup and reset
        self.active = True
        self.seed.occupations.clear()
        self.seed.events.clear()

        # open file
        with open(fn, 'r') as f:
            data = json.load(f)

        # integrity check
        if data['type'] != 'Seed':
            return

        # load things
        self.seed.occupations = data['occupations']
        self.seed.events = data['events']
        self.seed.names = data['names']

        # check integrity
        good = self.seed.check_integrity()
        if not good:
            return

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
            self.seed.occupations[f['title']] = f
        elif f['type'] == 'Event':
            self.seed.events[f['title']] = f
        elif f['type'] == 'Names':
            # merge new names into existing names
            # TODO: remove duplicates
            if 'male' in f:
                for name in f['male']:
                    self.seed.names['male'].append(name)
            if 'female' in f:
                for name in f['female']:
                    self.seed.names['female'].append(name)
            if 'last' in f:
                for name in f['last']:
                    self.seed.names['last'].append(name)
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
        if not good:
            return

        # header
        wdata['type'] = 'Seed'
        wdata['occupations'] = {}
        wdata['events'] = {}
        wdata['names'] = {}

        # insert data
        wdata['occupations'] = self.seed.occupations
        wdata['events'] = self.seed.events
        wdata['names'] = self.seed.names

        with open(fn, 'w') as f:
            json.dump(wdata, f)

    # ## town ## #

    def name_people(self, num_people):
        for i in range(0, num_people):
            print('Person: ' + str(i))
            tmp = Person()
            s = randint(0, 1)
            if s == 0:
                print('  male')
                tmp.sex = 'm'
                f = randint(0, len(self.seed.names['male']) - 1)
                tmp.fname = self.seed.names['male'][f]
            else:
                print('  female')
                tmp.sex = 'f'
                f = randint(0, len(self.seed.names['female']) - 1)
                tmp.fname = self.seed.names['female'][f]
            print('  first name: ' + tmp.fname)
            ln = randint(0, len(self.seed.names['last']) - 1)
            tmp.fname = self.seed.names['last'][ln]

            o = randint(0, len(self.seed.occupations) - 1)
            tmp.ocupation = 'j'

            self.citizens.append(Person())

    def gen_town(self, num_people, num_years, tname, filename):
        self.name = tname
        self.name_people(num_people)

        for i in range(0, num_years):  # loop on number of years
            for j in range(0, num_people):
                r = randint(0, 4)
                if r == 4:
                    r = randint(0, 9)
                    if r < 6:
                        print('Giving an event 1')  # pick an event
                    elif r < 9:
                        print('Giving an event 2')  # pick a 2
                    else:
                        print('Giving an event 3')  # pick a 3

            # after everything generated, export
            # self.export(filename)

    def new(self):
        self.name = ''
        self.citizens.clear()
        self.events.clear()

    def clear(self):
        self.active = False

    def getPath(self, pathkey):
        if pathkey in self.mods:
            return self.mods[pathkey]['path']
        else:
            return ''

    def export(self, fn):
        self.data = {}

        if self.active:
            # make changes
            self.data['name'] = self.name
            self.data['population'] = self.population
            self.data['people'] = self.citizens

            for i in range(0, len(self.citizens)):
                self.data['people'][i.name] = {}

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
