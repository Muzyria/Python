
with open("class_scores.txt", "r", encoding='utf-8') as file_r, \
        open("new_scores.txt", "w", encoding='utf-8') as file_w:
    for line in file_r:
        file_w.write(f'{line.split()[0]} {int(line.split()[1]) + 5 if int(line.split()[1]) < 95 else 100}\n')
