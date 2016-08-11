# coding:utf-8


def paramer_decorater(func):
    print "i will show before wrapper"
    def _wrapper():
        print "i am wrapper"
        func()
    return _wrapper

@paramer_decorater
def origin_func():
    print "i am origin guy"
        
origin_func()
    
    

