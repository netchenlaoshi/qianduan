import unittest
from unittest import mock


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value='1584684322970')
        self.assertEqual('1584684322970',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15846843229702')
        self.assertEqual('15846843229702',get_salt())

    def test_get_sign(self):
        self.assertEqual('675ff9174c055d8393e20bb793d78af3',get_sign)

if __name__ == '__main__':
    unittest.main()
