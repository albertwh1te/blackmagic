class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ans = 0
        while n >= x:
            ans += n / x
            x *= 5
        return ans

test = Solution()
print(test.trailingZeroes(10))
