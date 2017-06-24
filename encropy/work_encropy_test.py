# -*- coding: utf-8 -*-
from Crypto.Cipher import Blowfish
import json

unpad = lambda s: s[0:-ord(s[-1])]
def PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    appendage = chr(packingLength) * packingLength
    return string + appendage

def PandoraDecrpt(string, key):
    c1 = Blowfish.new(key, Blowfish.MODE_ECB)
    return unpad(c1.decrypt(string))


def PandoraEncrypt(string,key):
    c1 = Blowfish.new(key, Blowfish.MODE_ECB)
    packedString = PKCS5Padding(string)
    return c1.encrypt(packedString)

if __name__ == '__main__':
    key= "1498187338000"[:10]
    # strt = """{"alias": "129;pgenius", "rows": [{"SEC_INNER_CODE": 101001085, "IMPACT": 4.0148, "CTIME": "2016-06-16 17:59:35", "GENIUS_UID": 10645997851, "TRADEDATE": "2016-06-16 00:00:00", "ISVALID": 1, "INNER_CODE": 106002628, "WEIGHT_PCT": 1.74, "SEQ": 18491200, "MTIME": "2016-06-17 14:33:52"}], "table": "ana_indx_impact_idx", "event": 1, "update": 1498037740005}"""

    strt = json.dumps({"alias": "129;pgenius", "rows": [{"sql": "BEGIN"}], "event": 4, "update": 1498187338000}).encode('utf-8')
    print(len(strt))
    enpstr = PandoraEncrypt(strt,key)
    text = PandoraDecrpt(enpstr,key)
    print(len(enpstr))
    print(enpstr)
    print(text)
