def reverse(input_str):

    if len(input_str) == 0:
        return input_str

    return input_str[-1]+reverse(input_str[0:-1])

c = reverse('hello')
print(c)
