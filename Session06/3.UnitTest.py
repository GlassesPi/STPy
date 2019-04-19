def OddEven(x):
    if x <= 0:
        return 'invalid'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'

import unittest

class OddEvenTester(unittest.TestCase):
    def test_even(self):
        self.assertEqual(OddEven(4), 'even')
    def test_odd(self):
        self.assertEqual(OddEven(5), 'odd')
    def test_invalid(self):
        self.assertEqual(OddEven(-1), 'invalid')
    def test_all(self):
        self.ass

unittest.main()