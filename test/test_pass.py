import unittest
from testing.pass_lib import *

class TestPass(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)

if __name__ == '__main__':
    unittest.main
