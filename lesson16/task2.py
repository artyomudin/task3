def in_range(start, end ,step, num):
    for i in range(start, end , step):
        yield i**num

my_list = []
c = in_range(1, 11,2, 2)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

