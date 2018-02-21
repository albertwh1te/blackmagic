class A:
    def __init__(self,value):
        self.value  = value
    def __add__(self,b):
        self.value = b.value + self.value
        return self
