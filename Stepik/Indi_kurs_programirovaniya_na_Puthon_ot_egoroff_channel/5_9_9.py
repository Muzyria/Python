phrase = 'Take only the words that start with t in this sentence'
print([x for x in phrase.split() if x[0] == 't' or x[0] == 'T'])