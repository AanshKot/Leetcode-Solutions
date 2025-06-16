# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levels = []

        q = deque()

        q.append(root)

        while len(q) > 0:
            #1. get the length of the queue this will represent the current length of our level
            lengthLevel = len(q)
            level = [] #represents the node values in the level
            
            for i in range(lengthLevel):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level)

        return levels

