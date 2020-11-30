import unittest
from testing.fail_lib import *

class TestPass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), -1)

    def test_sub(self):
        self.assertEqual(sub(1, 2), 3)

if __name__ == '__main__':
    unittest.main
