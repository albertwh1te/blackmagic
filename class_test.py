class testA():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def call(self):
        print(self.name,self.age)
    def fuck(self):
        print('haha')

tom = testA("tom",22)
tom.call()
tom.fuck()

sisi = testA("sisi",35)
sisi.call()
sisi.fuck()