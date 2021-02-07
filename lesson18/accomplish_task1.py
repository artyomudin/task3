from task1 import make_odd_list as func

def get_square_nums(my_func):
    square_list = [s_num**2 for s_num in my_func]
    return square_list

b = get_square_nums(func(1,50,2))
print(b)