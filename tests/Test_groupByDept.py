import unittest
from Library.notice_board import groupByDept

class TestTest(unittest.TestCase):
    def test_in_string(self):
        obj = groupByDept('333')
        val = [[333003], [333006], [333007]]
        self.assertEqual(val, obj)

    def test_notin_string(self):
        obj = groupByDept('333')
        val = [[666666], [111111], [999999]]
        self.assertNotEqual(val, obj)