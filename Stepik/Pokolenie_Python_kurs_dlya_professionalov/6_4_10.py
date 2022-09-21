from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    for elm in obj:
        print(f'name: {elm.name}', f'family: {elm.family}', f'sex: {elm.sex}', f'color: {elm.color}', sep='\n')
        print()
