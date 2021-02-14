def is_pallindrome(looking_string):
    if len(looking_string) <= 1:
        return True
    if looking_string[0] != looking_string[-1]:
        return False
    return is_pallindrome(looking_string[1:-1])



b = is_pallindrome('ssassass')
print(b)
m = is_pallindrome('mom')
print(m)
o = is_pallindrome('o')
print(o)