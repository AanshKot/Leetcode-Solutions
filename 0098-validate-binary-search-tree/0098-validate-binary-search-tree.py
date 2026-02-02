# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for left side DFS maintain curMin if any value in the left side dfs exceeds the m in
        #for each traversal maintain curMin, curMax (initially equal to value at rootNode)
        
        # if any rightTree traversal falls below curMin return False
        # set new curMax if the right node exceeds curMax

        # if any leftTree traversal exceeds curMax return False
        # if falls below curMin set new curMin

        
        def dfs(root, curMin, curMax):
            if root:
                if(curMin < root.val < curMax):
                    leftSubtree = dfs(root.left, curMin, root.val)
                    rightSubtree = dfs(root.right, root.val, curMax)
                    return leftSubtree and rightSubtree
                else: 
                    return False

            return True

        return dfs(root, float('-inf'), float('inf'))