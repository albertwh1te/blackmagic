class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num in [2,3,5]:
            return True
        elif num >1 and num not in [2,3,5]:
            a = ([i, num//i] for i in range(1, int(num**0.5)+1) if num % i == 0)
            factors = set(reduce(list.__add__,a))
            print factors
            print factors.difference([1,num]).difference([2,3,5])
            if factors.difference([1,num]).difference([2,3,5]) == set([]):
                return True
            else:
                return False
    
            
t = Solution()
print t.isUgly(2)    
# print t.isUgly(6)    
print t.isUgly(7)    
print t.isUgly(9)    

        
    
        
        