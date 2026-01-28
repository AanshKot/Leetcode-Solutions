# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()

        rightSideView = []

        q.append(root)
        while len(q) > 0:
            level = []
            levelLength = len(q)
            
            for i in range(levelLength):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            rightSideView.append(level[-1])
        
        return rightSideView



            

        