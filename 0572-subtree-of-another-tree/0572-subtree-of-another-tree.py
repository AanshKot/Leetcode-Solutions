# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        #subRoot == NULL means its a subset of all possible trees
        if not subRoot:
            return True

        #root == NULL and subRoot existing => Null cannot superset anything
        if not root:
            return False
        
        if (self.sameTree(root, subRoot)):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        
        leftSubtree = self.sameTree(p.left, q.left)
        rightSubtree = self.sameTree(p.right, q.right)

        return leftSubtree and rightSubtree