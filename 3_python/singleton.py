# simple singleton
# usage reduce memory cost

class Singleton(object):

    _singleton = None
    def __new__(cls,*args,**kwargs):
        if not cls._singleton:
           cls._singleton = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._singleton


a = Singleton()
b = Singleton()
print(a)
print(b)
print(a)
print(a == b)

