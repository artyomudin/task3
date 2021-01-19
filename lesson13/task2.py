#method = 'up'
def myfunc(func):
    return func

def thefunc(word, method):
    if method == 'up':
        print(word.upper())
    elif method == 'down':
        print(word.lower())
    else:
        print('what?')

def somefunc(*args, multiplier=2):
    mylist = [num*multiplier for num in args]
    print(mylist)



myfunc(thefunc('DEllo', 'hs'))
myfunc(somefunc(2,3,5,4,8, multiplier=5))