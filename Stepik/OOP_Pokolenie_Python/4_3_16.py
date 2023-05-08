class Knight:
    X = 'abcdefgh'
    Y = '87654321'

    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = Knight.X.index(horizontal)
        self.vertical = Knight.Y.index(str(vertical))
        self.color = color
        self.board = [['.'] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if i == self.vertical and j == horizontal:
                    self.board[i][j] = 'N'
                if abs(self.horizontal - j) * abs(self.vertical - i) == 2:
                    self.board[i][j] = '*'


    def get_char(self):
        return 'N'

    def can_move(self, *coordinate):
        x1, y1, x2, y2 =

        if ((x1 - x2) * (y1 - y2)) == 2 or ((x1 - x2) * (y1 - y2)) == -2:
            print('YES')
        else:
            print('NO')

    def move_to(self):
        pass

    def draw_board(self):
        [print(*row) for row in self.board]


# knight = Knight('c', 3, 'white')
#
# print(knight.color, knight.get_char())
# print(knight.horizontal, knight.vertical)
# # white N
# # c 3
#
# knight = Knight('c', 3, 'white')
#
# print(knight.horizontal, knight.vertical)
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))
#
# knight.move_to('e', 4)
# print(knight.horizontal, knight.vertical)
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
