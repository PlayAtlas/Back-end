import unittest
import superlist as sl

class TestInputValidation(unittest.TestCase):
    def compare(self, mylist1, mylist2):
        self.assertEqual(mylist1, mylist2) #сравниваем суммы элементов
        for i in range(len(mylist1)): #сравниваем поэлементно:
            self.assertEqual(mylist1[i], mylist2[i])

    def test_arithmetic(self):
        mysuperlist1_backup = sl.CustomList([1, 2])
        mysuperlist1 = sl.CustomList([1, 2])
        mysuperlist2 = sl.CustomList([2, 3, 5])
        sumsuperlist = mysuperlist1 + mysuperlist2
        subsuperlist1 = mysuperlist1 - mysuperlist2
        subsuperlist2 = mysuperlist2 - mysuperlist1
        #проверка сложения и вычитания для двух CustomList
        self.compare(sumsuperlist, sl.CustomList([3, 5, 5]))
        self.compare(subsuperlist1, sl.CustomList([-1, -1, -5]))
        self.compare(subsuperlist2, sl.CustomList([1, 1, 5]))
        
        #проверка типа результата арифметических действий
        self.assertEqual(type(sumsuperlist), sl.CustomList)
        self.assertEqual(type(subsuperlist1), sl.CustomList)
        self.assertEqual(type(subsuperlist2), sl.CustomList)

        #проверка сложения для CustomList из 2 и списка из 1
        self.compare(mysuperlist1 + [55], [56,2])
        self.compare([55] + mysuperlist1, [56,2])
        #проверка сложения для CustomList из 2 и списка из 3
        self.compare(mysuperlist1 + [-2, 0, 38], [-1, 2, 38])
        self.compare([-2, 0, 38] + mysuperlist1, [-1, 2, 38])

        #проверка вычитания для CustomList из 2 и списка из 1
        self.compare(mysuperlist1 - [-4, 75, 6], [5, -73, -6])
        self.compare([-4, 75, 6] - mysuperlist1, [5, -73, -6])

        #проверка вычитания для CustomList из 2 и списка из 3
        self.compare(mysuperlist1 - [-4, 75, 6], [5, -73, -6])
        self.compare([-4, 75, 6] - mysuperlist1, [5, -73, -6])

        #проверка неизменности
        self.compare(mysuperlist1, mysuperlist1_backup)
        
    def test_comparisons(self):
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