def choose_func(mylist:list):
    if min(mylist)>0:
        return sqare_nums(mylist)
    else:
        return remove_negatives(mylist)



def sqare_nums(mylist):
    return [num**2 for num in mylist]

def remove_negatives(mylist):
    return [num for num in mylist if num >0]

print(choose_func([-1,2,-6,5]))
