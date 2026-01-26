# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #if p is less than the root and q is greater than the root 
        #we know automatically that the root is the lowest common ancestor

        #if both p and q are less than the root traverse left

        #if both p and q are greater than the root traverse right

        #now the case where the root node is equivalent to either p or q and passes all the earlier conditions
        #the node is allowed to be a descendant of itself so we can return than node

        cur = root

        while True:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            else:
                return cur
            