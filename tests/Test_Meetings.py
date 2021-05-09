import unittest
from Library.meetings import showMeetings

class TestTest(unittest.TestCase):
    def test_in_string(self):
        obj = showMeetings()
        val = ['meeting on sunday']
        self.assertEqual(val, obj[0])

    def test_notin_string(self):
        obj = showMeetings()
        val = ['not in string']
        self.assertNotEqual(val, obj[0])

