def sum_of_digits(digit_str):

    if len(digit_str) == 0:
        return 0
    if not digit_str.isdigit():
        raise ValueError("input string must be digit string")
    return sum_of_digits(digit_str[0:-1]) + int(digit_str[-1])


c = sum_of_digits('test')
print(c)
