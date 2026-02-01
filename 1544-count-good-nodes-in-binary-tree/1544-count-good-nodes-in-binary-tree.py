# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root, curMax):
            if not root:
                return

            if root.val >= curMax:
                res[0] += 1
            
            dfs(root.left, max(curMax, root.val))
            dfs(root.right,max(curMax, root.val))
        
        dfs(root, root.val)
        return res[0]