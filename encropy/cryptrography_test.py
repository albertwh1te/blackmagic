# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"this is a test 1: 上九潜龙勿用")
print(f.decrypt(token))
