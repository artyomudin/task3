import unittest
import task2


class PersDataTastCase(unittest.TestCase):

    def SetUp(self):
        self.book = {'name':'Johnny',
        'surname':'Cash',
        'phonenumber':'0001122',
        'city':'Memphis',
        }

    def test_pers_data(self):
        cont = task2.get_pers_data('Johnny', 'Cash', '0001122', 'Memphis')
        res = self.book
        self.assertEqual(cont, res)


unittest.main()
