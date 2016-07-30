# -*- coding: utf-8 -*-
class Solution(object):
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]
            
        """
        :type n: int
        :rtype: int
        """
        """
    设 f (n) 表示爬 n 阶楼梯的不同方法数，为了爬到第 n 阶楼梯，有两个选择：
• 从第 n  - 1 阶前进 1 步；

• 从第 n  - 2 阶前进 2 步；

因此，有 f (n) = f (n  - 1) + f (n  - 2)。

这是一个斐波那契数列。
        """

t = Solution()
print t.climbStairs(2)
print t.climbStairs(3)
        
            