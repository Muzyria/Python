

class Wordplay:
    def __init__(self, words=None):
        if not words:
            words = []
        self.words = words[:]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [el for el in self.words if len(el) == n]

    def only(self, *args):
        return [el for el in self.words if all([char in args for char in set(el)])]

    def avoid(self, *args):
        return [el for el in self.words if all([char not in args for char in set(el)])]


wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))

wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))

wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))  # ['timur', 'geek', 'python', 'stepik']
