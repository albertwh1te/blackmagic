#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
PADDING = '\0'
#PADDING = ' '
pad_it = lambda s: s+(16 - len(s)%16)*PADDING
key = '1234567812345678'
iv = '1234567812345678'
source = 'Test String'
# generator = AES.new(key, AES.MODE_CBC, iv)
generator = AES.new(key, AES.MODE_CBC,iv)
crypt = generator.encrypt(pad_it(source))
cryptedStr = base64.b64encode(crypt)
print cryptedStr
generator = AES.new(key, AES.MODE_CBC,iv)
recovery = generator.decrypt(crypt)
print recovery.rstrip(PADDING)

