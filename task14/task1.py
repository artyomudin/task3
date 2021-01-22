def logger_func(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} has attributes {args}.')
    return wrapper





def add(x, y):
    return x + y

def sqare_all(*args):
    my_list = [num**2 for num in args]
    return my_list

#print(add(5, 7))
#print(sqare_all(2,3,4,5))
#print(logger_func(add(4,5)))

@logger_func
def sqare_all(*args):
    my_list = [num**2 for num in args]
    return my_list

@logger_func
def add(x, y):
    return x + y

sqare_all(5,6,7,8,9,1)
add(5,6)