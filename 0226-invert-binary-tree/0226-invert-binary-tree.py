# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            temp = root.right

            root.right = root.left
            root.left = temp
            
            #do this for the root's left and right children
            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
        return
        