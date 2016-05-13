class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        from collections import Counter
        for index,times in Counter(nums).items():
            if times == max(Counter(nums).values()):
                 result = index
        return result
        
            
            
t = Solution()
print t.majorityElement([5,5,5,5,7])        
