class WordString:
    def __init__(self, string=""):
        self.__string = None
        self.string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        return len(self.string.replace("  ", " ").split())

    def __call__(self, indx, *args, **kwargs):
        return self.string.replace("  ", " ").split()[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
