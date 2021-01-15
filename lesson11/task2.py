class Mathematician:
    pass



    def square_nums(self, *nums):
        squares = [num**2 for num in nums]
        print(squares)

    def remove_positives(self, *nums):
        negatives = [num for num in nums if num < 0]
        print(negatives)

    def filter_leaps(self, *years):
        notleaps = [year for year in years if year % 4 != 0 and year % 100 != 0 and year % 400 != 0 ]
        print(notleaps)


math1 = Mathematician()
math1.square_nums(1,2,5,6,3)
math1.remove_positives(-1, 3, -5, 5, 0, -87, 56, 2)
math1.filter_leaps(2001, 1884, 1995, 2003, 2020)

