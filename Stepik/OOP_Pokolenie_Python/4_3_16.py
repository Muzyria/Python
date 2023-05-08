class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, *coordinate):
        pass

    def move_to(self):
        pass

    def draw_board(self):
        pass


knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)
# white N
# c 3

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
# c 3
# False
# True
# e 4

knight = Knight('c', 3, 'white')

knight.draw_board()
# ........
# ........
# ........
# .*.*....
# *...*...
# ..N.....
# *...*...
# .*.*....
