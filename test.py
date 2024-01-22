import unittest
from main import triplesum2zero

class TestSum2Zero(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(triplesum2zero([]), [])

    def test_single_zero(self):
        self.assertEqual(triplesum2zero([0, 0, 0]), [])

    def test_no_zero_sum(self):
        self.assertEqual(triplesum2zero([1, 2, 3]), [])

    def test_zero_sum_exists(self):
        self.assertEqual(triplesum2zero([-1, 0, 1]), [(-1, 0, 1)])

    def test_multiple_zero_sums(self):
        self.assertEqual(triplesum2zero([-1, 0, 1, -2, -1, 3]), [(-2, -1, 3), (-1, 0, 1)])

    def test_zero_sum_with_duplicates(self):
        self.assertEqual(triplesum2zero([-1, 0, 1, -1, 0, 1]), [(-1, 0, 1)])

if __name__ == '__main__':
    unittest.main()