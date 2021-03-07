from builtins import *

def caesar_alg(data, key=5):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'



#    data = input('input a phrase here: ')
#    key = int(input('input a key here: '))
    val_low = data.lower()
    vald = ''

    for letter in val_low:
        position = (alphabet.find(letter))
        new_position = position + key
        if letter in alphabet:
            vald = vald + alphabet[new_position]
        else:
            vald = vald + letter

    print(vald)

