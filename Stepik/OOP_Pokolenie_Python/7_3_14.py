class LowerString(str):
    def __new__(cls, string=''):
        instance = super().__new__(cls, str(string).lower())
        return instance


print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
