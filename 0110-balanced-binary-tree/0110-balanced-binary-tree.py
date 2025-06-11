# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        result = [True]

        def dfs(root):
            if not root:
                return 0

            leftSubtreeMaxDepth = dfs(root.left)
            rightSubtreeMaxDepth = dfs(root.right)

            if(abs(leftSubtreeMaxDepth - rightSubtreeMaxDepth) > 1):
                result[0] = False
            
            return 1 + max(leftSubtreeMaxDepth, rightSubtreeMaxDepth)
        
        dfs(root)
        return result[0]