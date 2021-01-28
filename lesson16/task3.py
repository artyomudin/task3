class Mysquareiterator:

    def __init__(self, start, finish, step):
        self.ind = start
        self.finish = finish
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind > self.finish:
            raise StopIteration
        value = self.ind*5
        self.ind += self.step
        return value

c = Mysquareiterator(1, 11, 2)
for i in c:
    print(i)

def in_range(start, end ,step, num):
    for i in range(start, end , step):
        yield i**num

my_list = []
c = in_range(1, 11,2, 2)
for i in c:
    my_list.append(f'the result is {i}')

print(my_list[2])
print(my_list[4])

