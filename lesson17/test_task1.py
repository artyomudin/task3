import task1
import unittest

class NameTestCase(unittest.TestCase):

    def test_full_name(self):
        result = task1.full_name('johny', 'cash')
        self.assertEqual(result, 'Johny Cash')



    def test_get_squares(self):
        finding = task1.get_square([2,3,4,5])
        self.assertEqual(finding, [4,9,16,25])

unittest.main()
