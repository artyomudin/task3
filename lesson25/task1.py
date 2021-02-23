from builtins import list, bool, len, range, print
from typing import Any





def binary_search(array:list, item:Any) -> bool:
    start = 0
    stop = len(array)
    if len(array) == 0:
        return False

    middle = len(array) // 2
    if item == array[middle]:
        return True
    if item > array[middle]:
        return binary_search(array[middle+1:], item)
    else:
        return binary_search(array[:middle], item)




c = binary_search(range(1,100), 51)
print(c)

