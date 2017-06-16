# -*- coding: utf-8 -*-
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import Blowfish,AES

class BaseCipher(object):

    def __init__(self,key,cipher):
        self.block_size = cipher.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        # cipher object crypto
        self.cipher = cipher
        # true crypter for use

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(self.block_size)
        self.crypter = self.cipher.new(self.key,self.cipher.MODE_CBC,iv)
        return base64.b64encode(iv + self.crypter.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:self.block_size]
        self.crypter = self.cipher.new(self.key,self.cipher.MODE_CBC,iv)
        return self._unpad(self.crypter.decrypt(enc[self.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


def cipher_factory(key,cipher_name):
    if cipher_name == "Blowfish":
        return BaseCipher(key,Blowfish)
    if cipher_name == "AES":
        return BaseCipher(key,AES)

if __name__ == '__main__':
    # cipher = cipher_factory('test',"AES")
    cipher = cipher_factory('test',"Blowfish")
    plain_text = "this is a long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long text"
    encrypted = cipher.encrypt(plain_text)
    text = cipher.decrypt(encrypted)
    print(text)
