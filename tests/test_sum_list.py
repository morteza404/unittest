import sys

path = "/home/shahbazi/Desktop/project"

if path not in sys.path:
    sys.path.insert(0, path)

from apps import sum_list
import unittest

class TestSumList(unittest.TestCase):
    def test_sum_pass(self):
        result = sum_list.sum_elements([1,2,3])
        self.assertEqual(result, 6)

    def test_sum_fail(self):
        result = sum_list.sum_elements([1,2,3])
        self.assertNotEquals(result, 5)
    