# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        # the current root, the aboveVal, isLeft bool
        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            
            #if the current node violates the left and right bounds set recursively by the parent
            # then we know the BST isn't valid
            if not (node.val < rightBound and node.val > leftBound):
                return False

            # every node in the left subtree has to be less than the parent
            # parent is set to the right boundary
            leftSub = dfs(node.left, leftBound, node.val)

            #every value in the right subtree has to be greater than the parent
            rightSub = dfs(node.right, node.val, rightBound)

            return leftSub and rightSub

        #no restrictions on what the root value can be (i.e no bounds on the root value)
        return dfs(root, float('-inf'), float('inf'))
