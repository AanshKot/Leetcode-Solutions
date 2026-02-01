# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        if not root:
            return res[0]

        
        def dfs(root, pathMax):
            if root:
                if root.val >= pathMax:
                    res[0] = res[0] + 1
                
                dfs(root.left, max(root.val, pathMax))
                dfs(root.right, max(root.val, pathMax))

                return

            return

        dfs(root, root.val)
        return res[0]