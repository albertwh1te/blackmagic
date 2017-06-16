# -*- coding: utf-8 -*-
from blowfish import BlowfishCipher
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

from Crypto.Cipher import Blowfish
import binascii

# See @falsetru answer for the following method
#
def PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    appendage = chr(packingLength) * packingLength
    return string + appendage

def PandoraEncrypt(string):
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    packedString = PKCS5Padding(string)
    return c1.encrypt(packedString)

def pandoraDecrpt(string):
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    return unpad(c1.decrypt(string))

if __name__ == '__main__':
    s = 'testings'
    oe = PandoraEncrypt(s)
    oe = binascii.hexlify(oe)
    print(oe)

    e = '223950ff19fbea872fce0ee543692ba7'
    e = binascii.unhexlify(e)
    c = pandoraDecrpt(e)
    print(c)
