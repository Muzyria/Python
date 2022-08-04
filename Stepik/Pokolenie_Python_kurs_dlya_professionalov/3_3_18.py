from datetime import datetime

notes = {}
pattern = '%d.%m.%Y; %H:%M'

with open('diary.txt', encoding='utf-8') as file:
    diary = file.read().split('\n\n')
    for note in diary:
        dt, text = note.split('\n', 1)
        dt = datetime.strptime(dt, pattern)
        notes[dt] = text

for dt, text in sorted(notes.items()):
    print(dt.strftime(pattern))
    print(text)
    print()

