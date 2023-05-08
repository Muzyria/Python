class Knight:
    def __init__(self, col, row, color):
        self.horizontal = col
        self.vertical = row
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, col, row):
        return (ord(self.horizontal) - ord(col)) ** 2 + (self.vertical - row) ** 2 == 5

    def move_to(self, col, row):
        if self.can_move(col, row):
            self.horizontal = col
            self.vertical = row

    def draw_board(self):
        for row in range(8, 0, -1):
            for col in 'abcdefgh':
                if self.horizontal == col and self.vertical == row:
                    print(self.get_char(), end='')
                elif self.can_move(col, row):
                    print('*', end='')
                else:
                    print('.', end='')
            print()


knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)
# white N
# c 3
#
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))
#
knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
# # c 3
# # False
# # True
# # e 4

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
knight = Knight('e', 5, 'black')

knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()
# ........
# ...*.*..
# ..*...*.
# ....N...
# ..*...*.
# ...*.*..
# ........
# ........
#
# ........
# ........
# ........
# ..*.*...
# .*...*..
# ...N....
# .*...*..
# ..*.*...
