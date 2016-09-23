# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        current = root
        tmp = current.right
        current.right = current.left
        current.left = tmp
        self.invertTree(current.left)
        self.invertTree(current.right)
