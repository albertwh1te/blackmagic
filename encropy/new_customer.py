# -*- coding: utf-8 -*-



def toBinary(s):
    return "".join(format(ord(x), 'b') for x in s)

def encrypt(s,key):
    b = toBinary(s)
    bitkey = toBinary(key)
    for i in range(len(b)):
        for j in b:
            reduce(lambda x:j^x,list(b))
