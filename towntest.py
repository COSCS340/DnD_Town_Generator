import sys
from utils.town import Town


# get command line arguments
cla = len(sys.argv)

if cla < 3:
    print(('Usage: towntest.py num_people num_years [pathtoseed]\n'
           'Running default: 5 people for 5 years of history'))
    nump = 5
    numy = 5
if cla == 3 or cla == 4:
    nump = int(sys.argv[1])
    numy = int(sys.argv[2])
if cla == 4:
    path = sys.argv[3]
else:
    path = ''

t = Town()

if path == '':
    t.seed_add('data/people/common/farmer.json')
    t.seed_add('data/names.json')
    t.seed_build('seeds/testseed.json')
    t.seed_load('seeds/testseed.json')
else:
    t.seed_load(path)

t.gen_town(nump, numy, "test town", "literallypointless.json")

print('TEST RESULTS:')

for i in t.citizens:
    print((f'NAME: {i.fname} {i.lname}\n'
           f'SEX: {i.sex}\n'
           f'LIFE?: {i.life}\n'))
