import unittest
from util import generate_random_array
from merge_sort import merge_sort
from quick_sort_2 import quick_sort
from radix_sort import radix_sort

def check_asc(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False

    return True
class TestSortMethods(unittest.TestCase):
    def test_merge_sort(self):
        results = []
        for _ in range(10):
            n = 20
            arr = generate_random_array(n)
            merge_sort(arr, 0, n-1)

            results.append(check_asc(arr))

        expected = [True] * 10
        self.assertEqual(results, expected)

    def test_quick_sort(self):
        results = []
        num_test = 20
        for _ in range(num_test):
            n = 30
            arr = generate_random_array(n)
            quick_sort(arr, 0, n-1)

            results.append(check_asc(arr))

        expected = [True] * num_test
        self.assertEqual(results, expected)

    def test_radix_sort(self):
        results = []
        num_test = 20
        for _ in range(num_test):
            n = 50
            arr = generate_random_array(n)
            arr = radix_sort(arr, 3)

            results.append(check_asc(arr))

        expected = [True] * num_test
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()
