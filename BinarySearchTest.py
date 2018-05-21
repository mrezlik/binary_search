import unittest

from BinarySearch import *

class BinarySearchTest(unittest.TestCase):

    def test_bad_number(self):
        binary_test = BinarySearch([1, 2, 33, 33, 12], 333)
        self.assertFalse(binary_test.binarySearch())

    def test_good_number(self):
        binary_test = BinarySearch([1, 2, 33, 33, 12], 2)
        self.assertTrue(binary_test.binarySearch())

if __name__ == '__main__':
    unittest.main()
