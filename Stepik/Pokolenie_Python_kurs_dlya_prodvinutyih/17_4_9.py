from random import randint

with open("random.txt", "w", encoding='utf-8') as file:
    for _ in range(25):
        file.write(f"{randint(111, 778)}\n")