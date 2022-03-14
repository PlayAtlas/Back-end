import unittest
import levfunc
class TestInputValidation(unittest.TestCase):

    def test_lev(self):
        self.assertEqual(levfunc.lfunc('a', 'a'), 0)
        self.assertEqual(levfunc.lfunc('a', 'b'), 1)
        self.assertEqual(levfunc.lfunc('aaa', 'a'), 2)
        self.assertEqual(levfunc.lfunc('a', 'bbb'), 3)
        self.assertEqual(levfunc.lfunc('a', 'bbb'), 3)
        self.assertEqual(levfunc.lfunc('11143411', '11117311'), 3)

if __name__ == '__main__':
    unittest.main()