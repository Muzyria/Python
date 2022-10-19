def remove_marks(text, marks):
    remove_marks.count += 1
    for i in marks:
        text = text.replace(i, "")
    return text

remove_marks.count = 0


# text = 'Hi! Will we go together?'
# print(remove_marks(text, '!?'))
# print(remove_marks.count)

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)
