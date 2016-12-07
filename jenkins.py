# coding:utf-8


def inverse_jenkins(key):
    key *= 2364026753
    key ^= (key >> 2)  ^ (key >> 4)  ^ (key >> 6)  ^ (key >> 8) ^ (key >> 10) ^ (key >> 12) ^ (key >> 14) ^ (key >> 16) ^ (key >> 18) ^ (key >> 20) ^ (key >> 22) ^ (key >> 24) ^ (key >> 26) ^ (key >> 28) ^ (key >> 30)
    key *= 3222273025
    key ^= (key >> 9) ^ (key >> 18) ^ (key >> 27)
    key *= 4042322161
    key ^= (key >> 22)
    key *= 16773121;
    return  key
print inverse_jenkins(1009365124)
