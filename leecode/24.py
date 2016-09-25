# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        third = head.next.next
        tmp1 = head
        tmp2 = head.next
        head = tmp2
        head.next = tmp1
        head.next.next = self.swapPairs(third)
        return head
