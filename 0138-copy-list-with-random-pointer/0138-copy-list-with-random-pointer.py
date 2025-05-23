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
        oldToCopy = { None: None } #base case where recieved node to be copied is None

        #first pass
        cur = head

        while cur:
            #1. copy the node to a new node
            #2. update the hashmap to map the old node to the copied
            #3. now the old node maps to the deep copied node 
            copiedNode = Node(cur.val)
            oldToCopy[cur] = copiedNode
            cur = cur.next
            #second pass
            
        #the old node's pointers act as the key for the values stored in the copied node
        cur = head

        while cur:
            #1. copy.next = oldToCopy[cur.next]
            #2. copy.random = oldToCopy[cur.random]

            #retrieve the copied node
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head] #head is an old node, there exists a copy of it



