
def arg_rules(max_length, contains):
    def decorator(func):

        def wrapper(name):
            if type(name) == str and len(name) < max_length and contains[0]  in name and contains[1] in name:
                return func(name)
            elif type(name) != str:
                print('wrong type')
            elif len(name) > max_length:
                print('wrong length')
            elif not contains[0] in name or not contains[1] in name:
                print('requires variables')
        return wrapper
    return decorator

@arg_rules(max_length = 15, contains =['@', '05'])
def create_slogan(name):
    return ('{} drinks pepsi in his new BMW.'.format(name.title()))

print(create_slogan('@sam05'))