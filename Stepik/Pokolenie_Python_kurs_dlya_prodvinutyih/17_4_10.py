
with open("input.txt", "r", encoding='utf-8') as file_r, open("output.txt", "w", encoding='utf-8') as file_w:
    for num, line in enumerate(file_r, 1):
        file_w.write(f'{num}) {line}')
