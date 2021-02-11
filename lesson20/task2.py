from typing import Any, Tuple, TypeVar


def test_type(x:Any, n:int = 10):
    res:Tuple[Any] = tuple(x for _ in range(n))
    return res

def square(x:int) -> int:
    return x**2

x = test_type(5)
print(x)
y = square('3')
print(y)



AnyStr = TypeVar('AnyStr', str, int, bytes)


def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b


c = concat('foo', 'fighters')
b = concat(25,52)
#a = concat('12', 25)
e = concat(b'foo', b'fighters')
print(c)
print(b)
#print(a)
d = concat(15, 15.0)
print(d)
print(e)