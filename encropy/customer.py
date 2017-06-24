# -*- coding: utf-8 -*-
import base64

def decrypt(s, key):
    s = base64.b64decode(s)
    str1 = ""
    ch = 0
    if len(key) == 0:
        return s
    elif s != key:
        for i in range(len(s)):
            j = i
            if j > len(key) -1:
                j  = j % len(key)
            ch = ord(s[i]) + 65535 - ord(key[j])
            if ch > 65535:
                ch = ch % 65535
                str1 += chr(ch)
    return str1

def encrypt(s,key):
    # str1 = ""
    str1 = u""
    ch = 0
    if len(key) == 0:
        return s
    elif s != "":
        for i in range(len(s)):
            j = i
            if j > len(key) -1:
                j = j % len(key)
            ch = ord(s[i])+ ord(key[j])
            if ch > 65535:
                ch = ch % 65535
            str1 += chr(ch)

    print(type(unichr(ch)))
    print(ch)
    print(str1)
    return base64.b64encode(str1)

# key  = "1234567890"

key = '1234567890123456'
origin = "testtesttest123"
enp = encrypt(origin,key)
# text = decrypt(enp,key)
text = decrypt("rFSUoJ6XqlpzUFNjZW1wppiXoZ2qqVlkWVKjoaqnV3BRja5WqKejWnNQU3WCgYJ/hVSwkWFWWZ2vlZ+mVW5Val1SVamlmpisnlJrUmRobm5jYmpoa2tna22t",key)
print(enp)
print(text)

