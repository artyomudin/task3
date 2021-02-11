from typing import Tuple, List


class Photo(object):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.tags:List[str]


'''class Photo(object):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
'''






def get_dimention(self) -> Tuple[int, int]:
    return self.width, self.height

if __name__ == '__main__':
    photo1 = Photo(110, 220)
    x = photo1.height
    print(x)