class Gun:
    def __init__(self):
        self.a, self.b = 'pif', 'paf'

    def shoot(self):
        print(self.a)
        self.a, self.b = self.b, self.a
