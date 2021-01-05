list_one = [2, 6, 5, 4, 8, 7, 85, 6, 5, 8]
list_two = [2, 3, 5, 4, 5, 86, 8, 7, 4, 5]

common_list = []
i = 0
while i < 10:
    if list_one[i] in list_two:
        common_list.append(list_one[i])
        i += 1
print(common_list)
