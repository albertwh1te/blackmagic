# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root
        # No Node No LCA
        if root is None:
            return None
        if current == p or current == q:
            return current
        else:
            new_p = self.lowestCommonAncestor(current.right, p, q)
            new_q = self.lowestCommonAncestor(current.left, p, q)
            if new_p and new_q:
                return root
            else:
                if new_p:
                    return new_p
                else:
                    return new_q
