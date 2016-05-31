class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 4:
            if num == 1:
                return True
            else:
                return False
        else:
            import math
            cc = round(math.log(num, 4))
            if num == (4 ** cc):
                return True
            else:
                return False
t = Solution()    
print t.isPowerOfFour(64)
print t.isPowerOfFour(16)
print t.isPowerOfFour(15)
print t.isPowerOfFour(-16)
print t.isPowerOfFour(2)
print t.isPowerOfFour(4)
print t.isPowerOfFour(6)