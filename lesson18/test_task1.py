import task1
import unittest

class NameTestCase(unittest.TestCase):
    def test_odd_list_getter(self):
        result = make_odd_list(1,11,2)
        self.assertEqual(result, ([3,9]))


if __name__ == '__main__':
    unittest.main()