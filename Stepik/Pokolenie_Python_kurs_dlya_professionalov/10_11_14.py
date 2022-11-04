from itertools import groupby


def group_anagrams(words):
    groups = groupby(sorted(words, key=lambda x: sorted(x)), key=lambda x: sorted(x))
    return [tuple(i[1]) for i in groups]


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)
# ('boko', 'book') ('evil', 'levi', 'live') ('afther', 'father')
