

class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        pass

    def only(self, *data):
        pass

    def avoid(self, data):
        pass


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


