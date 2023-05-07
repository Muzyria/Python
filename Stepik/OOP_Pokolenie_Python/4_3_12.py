class TextHandler:
    def __init__(self):
        self.my_list = []

    def add_words(self, word):
        self.my_list.extend(list(map(str, word.split())))

    def get_shortest_words(self):
        return [i for i in self.my_list if len(i) == len(min(self.my_list, key=len))]

    def get_longest_words(self):
        return [i for i in self.my_list if len(i) == len(max(self.my_list, key=len))]


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')
print(texthandler.my_list)

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
