with open('dataset_24465_4 (3).txt', "r") as file, \
        open('dataset_24465_4_reverse.txt.txt', "w") as file_2:

    f1_line = file.read().splitlines()

    for line in f1_line[::-1]:
        file_2.write(line + '\n')



