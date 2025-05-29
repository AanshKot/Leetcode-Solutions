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

        oldToCopy = {None:None}

        cur = head

        #first pass 
        while cur:
            #1. create the copied node
            copy = Node(cur.val)

            #2. map the cur node to the copy
            oldToCopy[cur] = copy

            #3. iterate current
            cur = cur.next

        #second pass, connect the nodes
        listRunner = head
        while listRunner:
            #get the copied node
            copy = oldToCopy[listRunner]

            #set the next pointer to the next node
                #how do we do this? we check the hashmap for key listRunner.next as the value has the copied node
            copy.next = oldToCopy[listRunner.next]
            copy.random = oldToCopy[listRunner.random]

            listRunner = listRunner.next
        
        return oldToCopy[head]

