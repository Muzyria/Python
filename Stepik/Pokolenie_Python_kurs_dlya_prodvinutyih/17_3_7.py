
with open("text.txt", "r", encoding='utf-8') as file:
    print(file.readline().rstrip()[::-1])
