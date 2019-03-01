def WhatDay(m, d):

    if m <= 7:
        s = (m - 1) * 31 + d
    else:
        s = (m - 1) * 30 + d + 6

    days = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]

    return days[s % 7]

import unittest

class WhatDayTester(unittest.TestCase):
    def test_Tue(self):
        self.assertEqual(WhatDay(5, 2), 'Tue')
    def test_Fri(self):
        self.assertEqual(WhatDay(12, 10), 'Fri')
    def test_Sat(self):
        self.assertEqual(WhatDay(11, 13), 'Sat')

unittest.main()