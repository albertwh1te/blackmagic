# -*- coding: utf-8 -*-
import binascii

def toBinary(s):
    print(int(binascii.hexlify(s),16))
    return bin(int(binascii.hexlify(s),16))

def decodeBinary(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# def toBinary(s):
#     return "".join(format(ord(x), 'b') for x in s)


def encrypt(s,key):
    b = toBinary(s)
    print(b)
    print(len(b))
    bitkey = toBinary(key)
    for i in range(len(b)):
        b[i] = str(reduce(lambda x,y:int(x)^int(y),list(bitkey),b[i]))
    return " ".join(b)


def decrypt(s,key):
    b = list(toBinary(s))
    dee = b
    bitkey = toBinary(key)
    for i in range(len(b)):
        b[i] = str(reduce(lambda x,y:int(x)^int(y),list(bitkey),dee[i]))
    return " ".join(b)

key = "fffffff"
s = "hi"
enc = encrypt(s,key)
text = decrypt(enc,key)
print(enc)
print(text)
