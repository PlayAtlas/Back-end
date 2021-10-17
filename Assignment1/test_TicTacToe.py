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
        self.assertFalse(tictac.validate_input([1, 2, 3]))
        self.assertFalse(tictac.validate_input([55, ]))
        self.assertFalse(tictac.validate_input('he he'))

    #def test_game(self):
     #   tictac = tictactoe.TicTacToe()
        #self.assertEqual(tictac.start_game(), 'X wins')



if __name__ == '__main__':
    unittest.main()