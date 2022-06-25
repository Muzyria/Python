class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
            print(*[f"{i[0]}.{i[1]}" for i in enumerate(self._notes, 1)], sep="\n")


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
