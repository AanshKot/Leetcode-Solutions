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
        
        if(self.isSameTree(root,subRoot)):
            return True
        
        leftSubtree = self.isSubtree(root.left, subRoot)
        rightSubtree = self.isSubtree(root.right, subRoot)

        return leftSubtree or rightSubtree

    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p and q:
            return False

        if not q and p:
            return False
        
        if p.val != q.val:
            return False
        
        leftSubtree = self.isSameTree(p.left, q.left)
        rightSubtree = self.isSameTree(p.right, q.right)

        return leftSubtree and rightSubtree

        