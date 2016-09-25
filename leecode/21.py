# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
                if l1 and l2:
            if l1.val < l2.val:
                new = l1
                right = l1.next
                left = l2
            else:
                new = l2
                left = l2.next
                right = l1
        elif l1:
            return l1
        else:
            return l2
        result = []
        result.append(new)
        while right and left:
            if right.val < left.val:
                new.next = right
                right = right.next
            else:
                new.next = left
                left = left.next
            new = new.next
        result.append(new)
        if right:
            new.next = right
        else:
            new.next = left
        if result:
            return result[0]
        else:
            return None
