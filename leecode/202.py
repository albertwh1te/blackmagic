class Solution(object):
    def __init__(self):
        self.past = set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        intermediate = sum(int(i) ** 2 for i in str(n))
        if intermediate == 1:
            return True
        elif intermediate in self.past:
            return False
        else:
            self.past.add(intermediate)
            return self.isHappy(intermediate)
            


t = Solution()
print t.isHappy(13)        
print t.isHappy(14)
print t.isHappy(20)
