"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneHash = {} #original node to copied node
        if not node:
            return None

        # this dfs is responsible for 
        # 1. if the node passed in has already been cloned
        # 2. return the cloned node, 
        def dfs(node):
            # original nodes are passed in each time we append a neighbour since we call cloneHash.append(originalNeighbourNode)
            # as such we will never be returning a copy in this scenario because the reference to the original node will never match the reference to a copy node

            if node in cloneHash:
                return cloneHash[node] # return the copied node
            
            #the node inputted to the DFS is an original node that hasn't been copied
            copy = Node(node.val)
            cloneHash[node] = copy

            for neighbour in node.neighbors:
                cloneHash[node].neighbors.append(dfs(neighbour))
            
            return copy

        copiedGraph = dfs(node)
        return copiedGraph
        
        