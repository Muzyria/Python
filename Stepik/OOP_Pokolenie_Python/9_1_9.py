class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = 'X'
        self.winner_symbol = None
        self.game_over = False

    def mark(self, row, col):
        if self.game_over:
            print('Игра окончена')
            return

        if not self._is_valid_move(row, col):
            print('Недоступная клетка')
            return

        self.board[row - 1][col - 1] = self.current_player
        self._check_winner()

        if not self.game_over:
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def winner(self):
        return self.winner_symbol

    def show(self):
        for i in range(3):
            print(f'{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}')
            if i < 2:
                print('-----')

    def _is_valid_move(self, row, col):
        return self.board[row - 1][col - 1] == ' '

    def _check_winner(self):
        # Проверка по горизонталям, вертикалям и диагоналям
        lines = self.board + list(zip(*self.board)) + [[self.board[0][0], self.board[1][1], self.board[2][2]],
                                                       [self.board[0][2], self.board[1][1], self.board[2][0]]]

        for line in lines:
            if line[0] == line[1] == line[2] != ' ':
                self.winner_symbol = line[0]
                self.game_over = True
                return

        # Проверка на ничью
        if all(cell != ' ' for row in self.board for cell in row):
            self.winner_symbol = 'Ничья'
            self.game_over = True
