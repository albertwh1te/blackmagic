# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curl = None
        while head != None:
            tmp = head.next
            head.next = curl
            curl = head
            head = tmp
        return curl
    
        
t = Solution()    
