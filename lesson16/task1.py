def with_index(iterable, start=0):
    my_dict = {}
    some_list = list(enumerate(iterable, start))
    for index, value in some_list:
        my_dict[index] = value
    print(my_dict)

some_list = ['marillion', 'manfred mann', 'pinc floyd', 'elo']

with_index(some_list, 1)