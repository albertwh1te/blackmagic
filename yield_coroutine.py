# coding:utf-8

def coroutine_yield():
    a = 0
    while a < 9:
        val = (yield a+1)
        a += 1
        print "now is %s " %val

c = coroutine_yield()
print c
print type(c)
print c.next()
print c.next()
print c.send(11)


