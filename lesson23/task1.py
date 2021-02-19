from builtins import print, bool, len, enumerate, reversed, str, property
from typing import List, Any


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    @property
    def reverse_print(self):
        temp_list = []

        if self.is_empty() == True and self.size() > 2:
            while self.size():
                for item in self._items:
                    var = self.pop()
                    temp_list.append(var)
        return temp_list


if __name__ == "__main__":
    s = Stack()

    s.push('hello')
    s.push('hi')
    s.push('bye')
    s.push('so long')
    s.push('hey')
    print(s)
    print(s.peek())
    print(s.reverse_print)
