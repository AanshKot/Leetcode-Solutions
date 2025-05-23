"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = { None: None }

        cur = head
        
        #first pass, cloning nodes
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy #map old node to copy node
            cur = cur.next

        #second pass
        cur = head
        while cur:
            copy =  oldToCopy[cur]
            copy.next = oldToCopy[cur.next] #the old node's next pointer is the key, the value is the copied old node's next pointer
            copy.random = oldToCopy[cur.random] #the old node's random pointer is the key that has the copied old node's random pointer
            cur = cur.next

        return oldToCopy[head] #head of old list is copied in hashmap and will be head of new list