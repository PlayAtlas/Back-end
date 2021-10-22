"""
Hometask №1: Making a TicTacToe game class
"""
class TicTacToe:
    grid = []
    count = {}
    player = ''

    def __init__(self, inpgrid = [' '] * 9, inpplayer = 'X', inpcount = {}):
        self.grid = inpgrid
        self.player = inpplayer
        self.count = inpcount
    
    def show_board(self):
        print('---------')
        for i in range(3):
            print('| ', end='')
            for j in range(3):
                print(self.grid[j + 3*i] + ' ', end='')
            print('|')
        print('---------')

    def validate_input(self, inp):
        if not isinstance(inp, str):
            print('Enter two numbers divided by one space')
            return False
        coords = inp.split()
        if len(coords) != 2 or not coords[0].isdigit() or not coords[1].isdigit():
            print('Enter two whole positive numbers divided by one space')
            return False
        x_coord = int(coords[0]) - 1
        y_coord = int(coords[1]) - 1
        if x_coord > 2 or x_coord < 0 or y_coord > 2 or y_coord < 0:
            print('Coordinates should be from 1 to 3!')
            return False
        if self.grid[y_coord*3 + x_coord] == 'X' or self.grid[y_coord*3 + x_coord] == 'O':
            print('This cell is occupied! Choose another one!')
            return False
        return True

    def start_game(self):
        self.grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.count = {'X': 0, 'O': 0}
        while True:
            self.show_board()
            # validating input
            play = input('Enter the coordinates:')
            while self.validate_input(play) is False:
                play = input('Enter the coords:')
            # pulling coords out of input
            coords = play.split()
            x_coord = int(coords[0]) - 1
            y_coord = int(coords[1]) - 1
            # making the play
            self.grid[y_coord*3+x_coord] = self.player
            self.count[self.player] += 1
            # checking if the game is finished
            if self.check_winner() != 0:
                break
            # switching player
            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'

    def check_winner(self):
        winner = 0
        if self.grid[0] == self.grid[4] == self.grid[8] != ' ':
            winner = self.grid[0]
        elif self.grid[2] == self.grid[4] == self.grid[6] != ' ':
            winner = self.grid[2]
        else:
            for i in range(3):
                if (self.grid[i*3] == self.grid[i*3+1] == self.grid[i*3+2] != ' '
				or self.grid[i] == self.grid[i+3] == self.grid[i+6] != ' '):
                    if winner == 0:
                        winner = self.player
        if winner == 0 and self.count['X'] + self.count['O'] == 9:
            winner = 'Draw'
            self.show_board()
            print(winner)
            return winner
        if winner != 0:
            self.show_board()
            print(winner, 'wins')
            return winner
        return 0


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
