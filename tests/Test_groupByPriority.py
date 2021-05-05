import unittest
from Library.notice_board import groupByPriority

class TestTest(unittest.TestCase):
    def test_in_string(self):
        obj = groupByPriority('5')
        val = [[333003], [777001], [333006]]
        self.assertEqual(val, obj)

    def test_notin_string(self):
        obj = groupByPriority('5')
        val = [[666666], [111111], [999999]]
        self.assertNotEqual(val, obj)