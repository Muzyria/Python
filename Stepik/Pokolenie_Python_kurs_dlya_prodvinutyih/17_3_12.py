# with open(r'C:\Users\Sasha\Downloads\file1.txt', 'r', encoding='utf-8') as file:
#     li = list(map(lambda x: x.strip(), file.readlines()))
#
#     lenli = len(li)
#
#     myString = ' '.join(li)
#     leter = 0
#     for i in myString:
#         if i.isalpha():
#             leter += 1
#
#     wordcount = myString.count(' ')
#
#     print('Input file contains:')
#     print(leter, 'letters' )
#     print(wordcount+1, 'words')
#     print(lenli, 'lines')

    # '''
    # with open('file1.txt') as file:
    #     text = file.read()
    #     print('Input file contains:')
    #     print(sum(map(lambda x: x.isalpha(), text)), 'letters')
    #     print(len(text.split()), 'words')
    #     file.seek(0)
    #     print(len(file.readlines()), 'lines')
    # '''

with open("file.txt", "r", encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]
    word = [i.split() for i in lines]
    amount_word = sum([len(i) for i in word])
    letters = [char for char in "".join(lines) if char.isalpha()]

    print("Input file contains:")
    print(f"{len(letters)} letters")
    print(f"{amount_word} words")
    print(f"{len(lines)} lines")
