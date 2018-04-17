from utils.town import Town

if __name__ == "__main__":
    t = Town()

    t.seed_add('data/people/common/farmer.json')
    t.seed_add('data/names.json')
    t.seed_build('testseed.json')

    t.seed_load('testseed.json')
    t.gen_town(50, 5, "test town", "literallypointless.json")

    print('TEST RESULTS:')

    for i in t.citizens:
        print((f'NAME: {i.fname} {i.lname}\n'
               f'SEX: {i.sex}\n'
               f'LIFE?: {i.life}\n\n'))
