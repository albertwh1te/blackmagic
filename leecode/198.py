class Solution(object):
    def rob_aux(self, nums, dict):
        if str(nums) in dict:
            return dict[str(nums)]

        if len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)

        one = nums[0] + self.rob_aux(nums[2:], dict)
        two = nums[1] + self.rob_aux(nums[3:], dict)

        if one > two:
            dict[str(nums)] = one
            return one
        else:
            dict[str(nums)] = two
            return two

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        return self.rob_aux(nums,dict)
