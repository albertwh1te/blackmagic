class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        low_price = prices[0]
        max_interests = 0
        for i in range(len(prices)):
            if low_price > prices[i]:
                low_price = prices[i]
            max_interests = max(max_interests, prices[i]-low_price)
        return max_interests      

t = Solution()    
print t.maxProfit([2,35,4,5])