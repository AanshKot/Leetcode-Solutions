# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #checks for invalidity of the current pointers/nodes p and q
        if not p and not q:
            return True #reached end of both trees

        if (p and not q) or (q and not p):
            return False
        
        if(p.val != q.val):
            return False
        
        #after all checks pass for the current node 
        #do this check for every subtree in the tree
        leftSubtree = self.isSameTree(p.left, q.left)
        rightSubtree = self.isSameTree(p.right, q.right)

        return leftSubtree and rightSubtree