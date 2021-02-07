def make_odd_list(start, finish, step):
    my_uneven_list = [num for num in range(start, finish, step) if num%3 == 0]
    return my_uneven_list


