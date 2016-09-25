# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                result =  root.left.val

        left = self.sumOfLeftLeaves(root.right)
        right = self.sumOfLeftLeaves(root.left)

        return left+right+result
