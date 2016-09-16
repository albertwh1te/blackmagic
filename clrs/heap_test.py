# coding:utf-8
# this scripts should run with python3

class hearp_obj(object):

    def __init__(self,arr):
        self.arr = arr

    def get_length(self):
        return len(self.arr)

    def get_parent(self,index):
        if (index & 1) == 0:
            return index//2 
        else:
            return index//2 

    def get_left(self,index):
        return index*2

    def get_right(self,index):
        return index*2+1
    
    def get_node(self,index):
        return self.arr[index-1]

a = hearp_obj([3,4,5,10,11,15])
print("inline heap:{}".format(a.arr))
print("get_length:{}".format(a.get_length()))
print("get_node 2:{}".format(a.get_node(2)))
print("get_left 2:{}".format(a.get_left(2)))
print("get_right 2:{}".format(a.get_right(2)))
print("get_parent 3:{}".format(a.get_parent(3)))
print("get_parent 4:{}".format(a.get_parent(4)))

