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
                return 0

            #if the root's value is greater than the curMax update the result
            if root.val >= curMax:
                res[0] += 1
                curMax = root.val

            #pre order traversal
            dfs(root.left, curMax)
            dfs(root.right, curMax)

        dfs(root, root.val)
        return res[0]