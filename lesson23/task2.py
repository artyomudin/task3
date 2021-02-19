from builtins import len, print


def define_brackets(srting):
    my_stack = []
    active = True
    for i in srting:
        if i in '([{':
            my_stack.append(i)
        elif i in ')]}':
            if not my_stack:
                active = False
                break

            bracket = my_stack.pop()
            if bracket == '(' and i == ')':
                continue
            if bracket == '{' and i == '}':
                continue
            if bracket == '[' and i == ']':
                continue
            active == False
            break



    if active and len(my_stack) == 0:
        print('ok')
    else:
        print('wrong bracket sequence')





c = define_brackets('({[]})')
print(c)
