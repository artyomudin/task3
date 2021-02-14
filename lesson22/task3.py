def mult(a, n):
    if n == 1:
        return a
    if n < 0 or a < 0:
        raise ValueError("This function works only with postive integers")
    return mult(a, n-1)+a

c = mult(4, -8)
print(c)