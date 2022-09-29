from collections import Counter


with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    text = [elm for elm in file.read().lower() if elm.isalpha()]
    [print(f'{k}: {v}') for k, v in Counter(sorted(text)).items()]
