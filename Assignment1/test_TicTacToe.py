import unittest
import tictactoe
#tictac = tictactoe.TicTacToe()
#print(tictac.validate_input('1 2'))
class TestInputValidation(unittest.TestCase):

    def test_input(self):
        tictac = tictactoe.TicTacToe()
        self.assertTrue(tictac.validate_input('1 2'))
        self.assertTrue(tictac.validate_input('2 3'))

        self.assertFalse(tictac.validate_input('22 55'))
        self.assertFalse(tictac.validate_input('4 2'))
        self.assertFalse(tictac.validate_input('1 5 6 2'))
        self.assertFalse(tictac.validate_input([2, 1]))
        self.assertFalse(tictac.validate_input('0, 1'))
        self.assertFalse(tictac.validate_input('2'))
        self.assertFalse(tictac.validate_input([1, 2, 3]))
        self.assertFalse(tictac.validate_input([55, ]))
        self.assertFalse(tictac.validate_input('he he'))

    def test_game(self):
        tictac = tictactoe.TicTacToe(['X', 'O', ' ', 'X', 'O', ' ', ' ', 'O', 'X'], 'O')
        self.assertEqual(tictac.check_winner(), 'O')

        tictac = tictactoe.TicTacToe(['X', ' ', 'O', 'O', 'X', ' ', 'X', 'O', 'X'], 'X')
        self.assertEqual(tictac.check_winner(), 'X')

        tictac = tictactoe.TicTacToe(['X', ' ', 'X', 'X', 'O', 'X', 'O', 'O', 'O'], 'O')
        self.assertEqual(tictac.check_winner(), 'O')

        tictac = tictactoe.TicTacToe(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'], 'X', {'X': 5, 'O': 4})
        self.assertEqual(tictac.check_winner(), 'Draw')
        

if __name__ == '__main__':
    unittest.main()