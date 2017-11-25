# -*- coding: utf-8 -*-

import struct

a = 20
b = 400

str = struct.pack("ii", a, b)  #转换后的str虽然是字符串类型，但相当于其他语言中的字节流（字节数组），可以在网络上传输
print 'length:', len(str)
print str
print repr(str)

#---- result
#length: 8
#    ----这里是乱码
#'/x14/x00/x00/x00/x90/x01/x00/x00'
