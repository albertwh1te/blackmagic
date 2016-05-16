class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        result = []
        for i in nums:
            if i in nums_dict:
                nums_dict[i] = 2
            else:
                nums_dict[i] = 1
    
        for i in nums_dict:
            if nums_dict[i] == 1:
                result.append(i)
    
        return result
    
t = Solution()
print t.singleNumber([1, 2, 1, 3, 2, 5])
