with open('lorem.txt', 'r', encoding='utf-8') as file:
    words = {}
    for line in file:
        for word in line.strip().upper().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    # print(words)
