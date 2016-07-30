class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] = 2
            else:
                nums_dict[i] = 1
        for i in nums_dict:
            if nums_dict[i] == 1:
                result = i
        return result
t = Solution()  
print t.singleNumber([2, 2, 1])
