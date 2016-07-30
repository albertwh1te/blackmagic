class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set([x for x in nums1 if x in nums2]))
t=Solution()
print t.intersection([2,3,4], [3,4,5])    