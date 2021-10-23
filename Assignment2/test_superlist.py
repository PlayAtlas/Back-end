import unittest
import superlist as sl

class TestInputValidation(unittest.TestCase):

    def test_arithmetic(self):
        mysuperlist1 = sl.CustomList([1, 2])
        mysuperlist2 = sl.CustomList([2, 3, 5])
        self.assertEqual(mysuperlist1 + mysuperlist2, [3, 5, 5])
        self.assertEqual(type(mysuperlist1 + mysuperlist2), sl.CustomList)
        self.assertEqual(type(mysuperlist1 - mysuperlist2), sl.CustomList)
        self.assertEqual(mysuperlist1 + [55], [56,2]) #для 3
        self.assertEqual([55] + mysuperlist1, [56,2])
        self.assertEqual(mysuperlist1 - [-4, 75, 6], [5, -73, -6])
        self.assertEqual([-4, 75, 6] - mysuperlist1, [5, -73, -6])

    def test_comparisons(self): #сделать для списков
        self.assertTrue(sl.CustomList([1, 2]) < sl.CustomList([2, 3, 5]))
        self.assertTrue([1, 2] < sl.CustomList([2, 3, 5]))
        self.assertTrue(sl.CustomList([1, 2]) < [2, 3, 5])

        self.assertTrue(sl.CustomList([1, 2]) <= sl.CustomList([2, 3, 5]))
        self.assertTrue([1, 2] <= sl.CustomList([2, 3, 5]))
        self.assertTrue(sl.CustomList([1, 2]) <= [2, 3, 5])

        self.assertTrue(sl.CustomList([1, 2]) == sl.CustomList([2, 1, 0]))
        self.assertTrue([1, 2] == sl.CustomList([2, 1, 0]))
        self.assertTrue(sl.CustomList([1, 2]) == [2, 1, 0])

        self.assertTrue(sl.CustomList([55,]) > sl.CustomList([2, 3, 5]))
        self.assertTrue([55,] > sl.CustomList([2, 3, 5]))
        self.assertTrue(sl.CustomList([55,]) > [2, 3, 5])

        self.assertTrue(sl.CustomList([56, 57]) >= sl.CustomList([1, 55, 55, 2]))
        self.assertTrue([56, 57] >= sl.CustomList([1, 55, 55, 2]))
        self.assertTrue(sl.CustomList([56, 57]) >= [1, 55, 55, 2])

        self.assertTrue(sl.CustomList([1, 2]) != sl.CustomList([2, 3, 5]))
        self.assertTrue([1, 2] != sl.CustomList([2, 3, 5]))
        self.assertTrue(sl.CustomList([1, 2]) != [2, 3, 5])

if __name__ == '__main__':
    unittest.main()