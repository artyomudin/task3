import datetime
class Exceptions:
    crutial_amount = 30
    def __init__(self):
       pass


class CustomExceptions(Exceptions):
    def __init__(self, hight, width, depth):
        self.hight = hight
        self.width = width
        self.depth = depth

    def represent_object(self):
        print('your object has dimensions {} to {} to {}.'.format(self.hight, self.width, self.depth))

    def zero_exception(self, n):
        try:
            print(Exceptions.crutial_amount / n)
        except ZeroDivisionError:
            with open('log.txt', 'a') as exc_file:
                exc_file.write('\n{} ZeroDivisionError'.format(datetime.datetime.now()))
            print('can\'t divide by zero')
        finally:
            print('are you content by the result?')


    def index_exception(self, index):
        params = [self.hight, self.width, self.depth]
        try:
            print(params[index])
        except IndexError:
            with open('log.txt', 'a') as exc_file:
                exc_file.write('\n{} IndexError'.format(datetime.datetime.now()) )
                print('you do not have such dimension')
        finally:
            print('how many dimensions do you have?')

    def key_error(self, key):
        m_dict = {'hight':self.hight, 'width':self.width, 'depth':self.depth}
        try:
            print(m_dict[key])
        except KeyError:
            with open('log.txt', 'a') as exc_file:
                exc_file.write('\n{} KeyError'.format(datetime.datetime.now()))
                print('check your key')
        finally:
            print('is that it?')


m1 = CustomExceptions(3,5,4)
m1.zero_exception(0)
m1.index_exception(3)
m1.key_error('width')
m1.represent_object()