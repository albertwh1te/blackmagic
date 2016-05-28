class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        cc = math.log(num, 4)
        if cc ** 4 == num:
            return True
        else:
            return False
t = Solution()
print t.isPowerOfFour(16)