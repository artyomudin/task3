"""from builtins import len, print, ValueError

my_list = [1, 2, 3, 4, 5]
new_list = []


def find_data(iter, data):
    mock_list = []
    var = ''
    var2 = ''
    while iter:

        if iter:
            var = iter.pop()
            print(var)
        if iter:
            var2 = iter.pop(0)
            print(var2)

            if var == data or var2 == data:
                return True

            else:
                mock_list.insert(0, var2)
                mock_list.append(var)

        if len(my_list) == 0:
            raise ValueError('item is not found!')


c = find_data(my_list, 5)
print(c)"""

from builtins import print, ValueError

from builtins import len, print

import self


class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"<Deque: `rear` {self._items} `front`>"

    def __str__(self):
        return self.__repr__()


    def get_from_stack(self, item):
        mock_list = []
        var = ''
        var2 = ''

        while self.size():
            if self.size() > 0:
                var = self.remove_front()
            if self.size() > 0:
                var2 = self.remove_rear()

                if var == item or var2 == item:
                    print('ok')
                    return True


                else:
                    mock_list.insert(0, var2)
                    mock_list.append(var)

            if self.size == 0:
                raise ValueError('item is not found!')




if __name__ == '__main__':
    d = Deque()
    d.add_front(1)
    d.add_front(2)
    d.add_front(3)
    d.add_front(4)
    d.add_front(5)
#    print(d)
    c = d.get_from_stack(3)
    print(c)
    print(d.__dict__)
