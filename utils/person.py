class Person:
    def __init__(self):
        self.meta = {}

        self.meta['name'] = None
        self.meta['birthday'] = None
        self.meta['age'] = -1
        self.meta['occupation'] = None
        self.meta['family'] = {}
        self.meta['family']['mother'] = None
        self.meta['family']['father'] = None
        self.meta['family']['spouse'] = None
        self.meta['family']['children'] = []

        self.life = []
        self.traits = []
