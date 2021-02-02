
class PhoneBook:
    main_dict = {
        'name':'somename',
        'surname':'somesurname',
        'phonenumber':'somenum',
        'city':'yourcity'
    }
    customers = []

    def __init__(self):
        self.__dict__ = PhoneBook.main_dict

    def get_pers_data(self, name, surname, phone, city):
        self.main_dict['name'] = name
        self.main_dict['surname'] = surname
        self.main_dict['phonenumber'] = phone
        self.main_dict['city'] = city
        PhoneBook.customers.append(self.main_dict)
        return PhoneBook.main_dict

    @classmethod
    def get_customers_list(cls):
        return PhoneBook.customers









c1 = PhoneBook()
b = c1.get_pers_data('Johnny', 'Cash', '0001122', 'Memphis')
print(b)
x = PhoneBook.get_customers_list()
print(x)




