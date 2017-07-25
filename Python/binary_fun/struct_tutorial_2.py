# -*- coding: utf-8 -*-


import struct
num = 1024
binary_data = struct.pack("<i",num)
print(binary_data)
int_data = struct.unpack("<i",binary_data)
print(int_data)

