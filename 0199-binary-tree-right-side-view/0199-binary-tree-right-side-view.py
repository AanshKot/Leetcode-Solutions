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
        
        #1. BFS (level order traversal)
        #2. append the rightmost element in the level to the res
            #a. the last element in the level is guaranteed to be the rightmost element in the tree
                #this is due to the fact that the level order traversal starts from the leftmost node and 
                #goes to the rightmost existing node

        q = deque()
        q.append(root)
        
        rightmostNodeVals = []
        
        while len(q) > 0:
            levelLength = len(q)
            level = []
            
            for i in range(levelLength):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            rightmostNodeVals.append(level[-1])

        return rightmostNodeVals
                

    