# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0] #store our max diameter

        def dfs(root):

            if not root:
                return 0
            
            #for each of the nodes we want the diameter and the height of the tree
            
            leftHeight = dfs(root.left) #calculate the left subtree height
            rightHeight = dfs(root.right)

            #compare diameter to stored cur max: res
            res[0] = max(res[0], leftHeight + rightHeight)

            return 1 + max(leftHeight,rightHeight) #find the max height of left and right subtree

        dfs(root)
        return res[0] 