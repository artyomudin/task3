from builtins import bool, len, enumerate, reversed, str, print, ValueError, Exception


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

    def get_from_stack(self, element):
        temp_list = []
        if self.is_empty() == True:

            while self.size():
                var = self.pop()
                print(var)
                temp_list.append(var)
                if var == element:
                    while temp_list:
                        unit = temp_list.pop()

                        self.push(unit)
                    return True
                if self.is_empty() == False:
                    raise ValueError








if __name__ == "__main__":
    b = Stack()
    b.push("1")
    b.push("2")
    b.push("3")
    b.push("4")
    b.push("5")
    z = b.get_from_stack('2')
    print(z)
