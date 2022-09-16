import pickle
import sys

data = [line.strip() for line in sys.stdin]

with open(data[0], 'rb') as file:
    func = pickle.load(file)
    print(func(*data[1::]))
