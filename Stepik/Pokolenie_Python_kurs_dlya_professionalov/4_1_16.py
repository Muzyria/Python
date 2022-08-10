import sys

data = [tuple(line.strip().split(' / ')) for line in sys.stdin]
word = data.pop()[0]
data = [line for line in data if line[1] == word]
data.sort(key=lambda x: (float(x[2]), x[0]))
[print(line[0], sep='\n') for line in data]
