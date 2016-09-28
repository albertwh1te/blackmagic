# coding : utf - 8


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i],nums[j+1] = nums[j+1], nums[i]
                j += 1

        return j+1

test = Solution()
print(test.removeDuplicates([1,2]))
print(test.removeDuplicates([1,1,2]))
print(test.removeDuplicates([1,1,1]))
