# coding:utf-8
class Solution(object):
    def getSum(self, a, b):
        while b:
            tmp = a & b
            a ^= b
            b = tmp <<1
            print b,bin(b)
        return a

t = Solution()
print t.getSum(11,3)

        
        
        
        
