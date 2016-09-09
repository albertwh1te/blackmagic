class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                results.append(i)
        return results
                
            
nums1=[1,3,4,5]
nums2=[3,4]
test = Solution()
print test.intersect(nums1,nums2)
