"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        originalToCopy = {}
        
        runner = head
        while runner:
            copy = Node(runner.val)
            originalToCopy[runner] = copy
            runner = runner.next

        runner2 = head
        while runner2:
            copy = originalToCopy[runner2]
            if runner2.next:
                copy.next = originalToCopy[runner2.next]
            else:
                copy.next = None

            if runner2.random:
                copy.random = originalToCopy[runner2.random]
            else:
                copy.random = None

            runner2 = runner2.next

        return originalToCopy[head]