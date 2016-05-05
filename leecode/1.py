class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in xrange(len(nums)):
            x = nums[i]
            if target-x in hash_dict:
                return [hash_dict[target-x], i]
            hash_dict[x] = i


t = Solution()
nums = [2, 7, 11, 15]
print t.twoSum(nums=nums, target = 9)

