class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        w = 0
        while i < (len(nums)-1):
            if nums[i] == 0:
                nums.pop(i)
                w += 1
            else:
                i += 1
        nums += w * [0]
        return nums




t = Solution()
print t.moveZeroes([0, 1, 0, 3, 12])
print t.moveZeroes([0,0,1])

