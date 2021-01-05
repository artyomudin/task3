file = open(r'C:\Users\ARTEM\PycharmProjects\pythonProject\file.txt', 'a', encoding='utf-8')
# s = file.readlines()
# print(s)
file.write('the song is nice\n')
file.write('the song is nice\n')
file.write('the song is nice')



print(file.read())
