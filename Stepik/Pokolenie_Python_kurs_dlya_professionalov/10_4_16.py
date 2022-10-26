class Alphabet:
    DI = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}

    def __init__(self, language):
        self.alp = iter(Alphabet.DI[language])
        self.language = language

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.alp)
        except StopIteration:
            self.alp = iter(Alphabet.DI[self.language])
            return next(self.alp)


ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(58)]
print(*letters)
