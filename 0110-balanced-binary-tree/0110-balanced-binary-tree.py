# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True];

        def dfs(root):
            if not root:
                return 0

            leftSubtree = dfs(root.left)
            rightSubtree = dfs(root.right)

            if(abs(leftSubtree - rightSubtree) > 1):
                res[0] = False

            return 1 + max(leftSubtree, rightSubtree)

        dfs(root)
        return res[0]
            





            
