# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderedArr = []

        # traverse the tree in order left -> root -> right
        # append node vals to a orderedArr result
        # return the k - 1 (since k is 1 indexed) element
        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                orderedArr.append(root.val)
                inOrderTraversal(root.right)

        inOrderTraversal(root)
        return orderedArr[k-1]
                
        