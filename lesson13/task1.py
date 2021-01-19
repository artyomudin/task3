def local_count(message = 'hi'):
    i = 0
    def somefunc(word = '|'):
        nonlocal i
        i+=1
        print(str(i)+ word+message+word)
    return somefunc

func = local_count('123')
print(func('%'))




