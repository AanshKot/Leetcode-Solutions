# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            
            leftHeight = dfs(root.left) #maxDepth of leftSubtree
            rightHeight = dfs(root.right) #maxDepth of rightSubtree

            res[0] = max(res[0], leftHeight + rightHeight) #combined leftHeight + rightHeight gives max diameter

            return 1 + max(leftHeight,rightHeight) #return the max depth of the subtree

        dfs(root)
        return res[0]