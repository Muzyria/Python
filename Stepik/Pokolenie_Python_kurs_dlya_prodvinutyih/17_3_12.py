with open(r'C:\Users\Sasha\Downloads\file.txt', 'r', encoding='utf-8') as file:
    li = list(map(lambda x: x.strip(), file.readlines()))

    lenli = len(li)

    myString = ' '.join(li)
    leter = 0
    for i in myString:
        if i.isalpha():
            leter += 1
    
    wordcount = myString.count(' ')

    print('Input file contains:')
    print(leter, 'letters' )
    print(wordcount+1, 'words')
    print(lenli, 'lines')

    '''
    with open('file.txt') as file:
    text = file.read()
    print('Input file contains:')
    print(sum(map(lambda x: x.isalpha(), text)), 'letters')
    print(len(text.split()), 'words')
    file.seek(0)
    print(len(file.readlines()), 'lines')
    '''