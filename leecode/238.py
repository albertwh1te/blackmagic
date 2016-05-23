class Solution(object):
    # output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        left = 1
        for i in range(len(nums)-1):
            left *= nums[i]
            output[i + 1] *= left
        right = 1   
        for i in range(len(nums)-1, 0, -1):
            right *= nums[i]
            output[i - 1] *= right
        return output
        

t = Solution()
# print t.productExceptSelf([1,2,3,4])    
# print t.productExceptSelf([0,2,3,4])    
print t.productExceptSelf([0, 0, 0, 0])  