# -*- coding: utf-8 -*-


xor = lambda x,y:x^y

def encrypt(text,key):
    bytetext = bytearray(text)
    bytekey = bytearray(key)
    # a ^ b ^ c = a ^ (b ^ c)
    key_xor_result = reduce(xor,bytekey)
    for i in range(len(bytetext)):
        bytetext[i] = xor(bytetext[i],key_xor_result)
