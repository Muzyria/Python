
def filter_anagrams(word, words):
    list_anagrams = []
    for item in words:
        if sorted(list(item)) == sorted(list(word)):
            list_anagrams.append(item)
    return list_anagrams


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
