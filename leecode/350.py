class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_arr = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    print nums1, nums2,new_arr
                    new_arr.append(nums2[1])
                    nums2[j] = nums1[j] = 0 
        return new_arr

nums1=[1,3,4,5]
nums2=[3,4]
test = Solution()
print test.intersect(nums1,nums2)
