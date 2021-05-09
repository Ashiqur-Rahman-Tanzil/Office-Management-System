import unittest
from Library.notice_board import groupByDate

class TestTest(unittest.TestCase):
    def test_in_string(self):
        obj = groupByDate()
        val = [[333006], [333007]]
        self.assertEqual(val, obj)

    def test_notin_string(self):
        obj = groupByDate()
        val = [[666666],[111111]]
        self.assertNotEqual(val, obj)