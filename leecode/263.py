class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num <= 0:
            return False
        else:
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
            return num == 1    
            
t = Solution()
print t.isUgly(2)    
print t.isUgly(6)    
print t.isUgly(7)    
print t.isUgly(9)    

        
    
        
        