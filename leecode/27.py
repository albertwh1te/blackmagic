class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val in nums:
            while val in nums:
                nums.remove(val)
        return len(nums)
    
t = Solution()
print t.removeElement([3, 3, 2, 3], 3)   