# coding:utf-8

class TestMe(object):

    def __init__(self,name):
        self.state = "init"
        self.name = name

    def __enter__(self):
        print(self.state)
        self.state = "I am in"
        print(self.state)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.state)
        self.state = "I am going out"
        print(self.state)
        print(self.name)



with TestMe("tom") as tm:
    aa = tm.name

print(aa)
