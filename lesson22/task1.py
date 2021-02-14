def to_power(x, exp):

   if exp < 0:
       raise ValueError('This function works only with exp > 0')
   if exp == 1:
       return x
   return to_power(x, exp-1)*x

c = to_power(2,-3)
print(c)

