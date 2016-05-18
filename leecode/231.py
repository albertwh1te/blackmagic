class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            import math
            test = round(math.log(n, 2))
            if 2 ** test == n:
                return True
            else:
                return False
        else:
            return False


t = Solution()
print t.isPowerOfTwo(6)
print t.isPowerOfTwo(-16)
print t.isPowerOfTwo(15)
print t.isPowerOfTwo(17)
