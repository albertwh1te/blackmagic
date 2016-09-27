class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        cc = math.log(n,3)
        if 3 ** cc == n:
            return True
        else:
            return False
