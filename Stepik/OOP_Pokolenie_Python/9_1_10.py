import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.open = False
        self.neighbours = 0

class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self._create_board()
        self._place_mines()
        self._calculate_neighbours()

    def _create_board(self):
        return [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]

    def _place_mines(self):
        positions = [(row, col) for col in range(self.cols) for row in range(self.rows)]
        mine_positions = random.sample(positions, self.mines)

        for row, col in mine_positions:
            cell = self.board[row][col]
            cell.mine = True

    def _calculate_neighbours(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                if cell.mine:
                    continue
                cell.neighbours = self._get_neighbours_count(row, col)

    def _get_neighbours_count(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr = row + dr
                nc = col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.board[nr][nc].mine:
                        count += 1
        return count
