# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
    
        if (self.isSameTree(root, subRoot)):
            return True

        leftSubtree = self.isSubtree(root.left, subRoot)
        rightSubtree = self.isSubtree(root.right, subRoot)

        return leftSubtree or rightSubtree

            
    
    def isSameTree(self, q, p):
        if not q and not p:
            return True
        if (q and not p) or (p and not q):
            return False
        
        if q.val != p.val:
            return False
        
        return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)

