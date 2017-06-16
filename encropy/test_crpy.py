#! /usr/bin/env python
#coding=utf-8

import struct
import hashlib
import random
import uuid

from Crypto.Cipher import AES,ARC2,Blowfish,CAST,DES,DES3
from util import time


def GenerageKey():
    import random
    import struct
    import hashlib
    seeds = random.random()
    m = hashlib.md5()
    m.update(str(seeds))
    ret1 = m.digest()
    seeds = random.random()
    m.update(str(seeds))
    ret2 = m.digest()
    ret = struct.pack("%ds%ds"%(len(ret1),len(ret2)),ret1,ret2)
    return ret

print(len(GenerageKey()))



key = GenerageKey()[:16]
# text = GenerageKey()[:16]
text = "this is test 1:上九潜龙勿用"

print(len(key),key)
# obj_list = [AES.new(key,AES.MODE_CBC),ARC2.new(key),Blowfish.new(key)]
obj_list = [AES.new(key,AES.MODE_CFB)]

for obj in obj_list:
  cryp = obj.encrypt(text)
  after = obj.decrypt(cryp)
  print(cryp,after)

