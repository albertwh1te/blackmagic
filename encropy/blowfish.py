# -*- coding: utf-8 -*-
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import Blowfish

class BlowfishCipher(object):

    def __init__(self, key):
        # setting up block size
        self.bs = Blowfish.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(self.bs)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:self.bs]
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[self.bs:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == '__main__':
    import time
    start_time = time.time()
    for i in range(1000):
        cipher = BlowfishCipher('test')
        # plain_test = "this is a test 1: 上九潜龙勿用"
        plain_text = "this is a long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long text"
        encrypted = cipher.encrypt(plain_text)
        text = cipher.decrypt(encrypted)
        print(text)
    end_timed = time.time()
    print(end_timed - start_time)
