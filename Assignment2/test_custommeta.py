import unittest
import custommeta as cm

class TestInputValidation(unittest.TestCase):

    def test_renaming(self):
        inst = cm.CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)

    def test_errors(self):
        inst = cm.CustomClass()
        #self.assertRaises(AttributeError, inst.x)
        #self.assertRaises(AttributeError, inst.val)
        self.assertRaises(AttributeError, inst.line)

if __name__ == '__main__':
    unittest.main()