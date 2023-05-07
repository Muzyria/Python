class Wordplay:
    def __init__(self, words=None):
        if not words:
            self.words = []
        else:
            self.words = words

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return [word for word in self.words if set(word).issubset(set(args))]

    def avoid(self, *args):
        return [word for word in self.words if not any(letter in word for letter in args)]


# wordplay = Wordplay()
#
# print(wordplay.words_with_length(1))
# print(wordplay.only('a', 'b', 'c'))
# print(wordplay.avoid('a', 'b', 'c'))
#
# wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])
# print(wordplay.only('o', 't'))

# wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])
# print(wordplay.avoid('a', 'b', 'c'))

words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)  # ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский', 'Гуев', 'Харисов', 'Светкин']
print(wordplay.words)  # ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
