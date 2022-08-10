
import sys


data = [line.strip() for line in sys.stdin if line.strip()[0] == '#']
print(len(data))

