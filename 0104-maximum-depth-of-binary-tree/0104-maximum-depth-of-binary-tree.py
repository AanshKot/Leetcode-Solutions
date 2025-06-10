# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # '1' is the current root, do this for every subtree, return the max between the left and right subtrees
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return 0
