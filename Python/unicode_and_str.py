# coding:utf-8

test_str = "测试"

print type(test_str),test_str

test_unicode = unicode(test_str, 'utf-8')

print type(test_unicode),test_unicode

with open("test.txt",'wb') as f:
    f.write(test_str)
#    f.write(test_unicode.decode('utf-8'))
f.close()

    
    









