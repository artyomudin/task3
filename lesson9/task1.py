'''with open('myfile.txt', 'w') as my_string:
    message = my_string.write('hello srting world')'''

with open('myfile.txt') as my_string:
    somefile = my_string.read()
    print(somefile)
