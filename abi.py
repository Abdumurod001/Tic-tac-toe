
# Tic Tac Toe
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print('| %s | %s | %s |' % (self.board[i], self.board[i + 1], self.board[i + 2]))
            print('-------------')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print('Invalid move')

    def check_win(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                self.winner = self.board[i]
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                self.winner = self.board[i]
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            return True
        return False

    def check_draw(self):
        if ' ' not in self.board:
            self.winner = 'draw'
            return True
        return False

    def play(self):
        while not self.check_win() and not self.check_draw():
            self.print_board()
            move = input('Player %s, select a position (0-8): ' % self.current_player)
            if move.isdigit() and int(move) in range(9):
                self.make_move(int(move))
            else:
                print('Invalid input')
        self.print_board()
        if self.winner == 'draw':
            print('The game is a draw!')
        else:
            print('Congratulations Player %s, you won!' % self.winner)

ttt = TicTacToe()
ttt.play()



