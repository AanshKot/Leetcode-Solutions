# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #look at notes (LC - tree section)

        # if no nodes in either the arrays
        if not preorder or not inorder:
            return None
        
        #root of our current subtree will always be the first element in our preOrder array
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        #value of mid will tell us how many values we want to the left of the root
        
        #preorder from index 1 to mid (exclusive)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root


        