class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def some_info(self):
        full_name = '{} {}'.format(self.name, self.surname)
        print('hello, my name is {} and i am {} years old.'.format(full_name, self.age))


per1 = Person('Johnny', 'Cash', 50)
Person.some_info(per1)
