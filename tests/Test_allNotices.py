import unittest
from Library.notice_board import allNotices

class TestTest(unittest.TestCase):
    def test_in_string(self):
        obj = allNotices()
        val = [[111005], [222004], [333003], [666002], [777001], [333006], [333007]]
        self.assertEqual(val, obj)

    def test_notin_string(self):
        obj = allNotices()
        val = [666666],[111111],[222222],[333333],[123456],[123444],[666333]
        self.assertNotEqual(val, obj)