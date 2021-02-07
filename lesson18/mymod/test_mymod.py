import count_lines as cl
import count_chars as cc



def test(name):

    cl.count_lines(name)
    cc.count_chars(name)




c =test('my_text.txt')
print(c)