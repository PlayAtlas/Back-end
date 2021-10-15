class TicTacToe:
	grid = list()
	count = dict()
	player = 'X'
	def show_board(self):
		print('---------')
		for i in range(3):
			print('| ', end='')
			for j in range(3):
				print(self.grid[j + 3*i] + ' ', end='')
			print('|')
		print('---------')

	def validate_input(self, inp):
		coordinates = inp.split()
		if len(coordinates) != 2 :
			print('Enter two numbers divided by one space')
			return False
		x = int(coordinates[0]) - 1
		y = int(coordinates[1]) - 1
		if x > 2 or x < 0 or y > 2 or y < 0:
			print('Coordinates should be from 1 to 3!')
		if self.grid[y*3 + x] == 'X' or self.grid[y*3 + x] == 'O':
			print('This cell is occupied! Choose another one!')
			return False
		return True

	def start_game(self):
		self.grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
		self.count = {'X': 0, 'O': 0, ' ': 0}
		while True:
			self.show_board()
			# validating input
			play = input('Enter the coordinates:')
			while self.validate_input(play) != True:
				play = input('Enter the coordinates:')
			# pulling coords out of input
			coordinates = play.split()
			x = int(coordinates[0]) - 1
			y = int(coordinates[1]) - 1
			# making the play
			self.grid[y*3+x] = self.player
			self.count[self.player] += 1
			# checking if the game is finished
			if self.check_winner() != 0:
				break
			# switching player
			if self.player == 'X':
				self.player = 'O'
			else:
				self.player = 'X'



	def check_winner(s):
		winner = 0
		if s.grid[0] == s.grid[4] == s.grid[8] != ' ':
			winner = s.grid[0]
		elif s.grid[2] == s.grid[4] == s.grid[6] != ' ':
			winner = s.grid[2]
		else:
			for i in range(3):
				if s.grid[i*3] == s.grid[i*3+1] == s.grid[i*3+2] != ' ' or s.grid[i] == s.grid[i+3] == s.grid[i+6] != ' ':
					if winner == 0:
						winner = s.grid[i*3]
		if winner == 0 and s.count['X'] + s.count['O'] == 9:
			print('Draw')
			return True
		elif winner != 0:
			s.show_board()
			print(winner, 'wins')
			return True
		else:
			return 0


if __name__ == '__main__':
	game = TicTacToe()
	game.start_game()
	
