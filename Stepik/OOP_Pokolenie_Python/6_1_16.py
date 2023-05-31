class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        self.junior.extend(args)

    def add_senior(self, *args):
        self.senior.extend(args)

    def __iter__(self):
        yield from [(names, 'junior') for names in self.junior]
        yield from [(names, 'senior') for names in self.senior]


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')
