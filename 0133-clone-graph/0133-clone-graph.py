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

        cloneHash = {}

        if not node:
            return None

        def dfs(node):
            #the base case is that the node has already been traversed and cloned
            #in this case we want to return the copied node
            # return the copied node
            if node in cloneHash:
                return cloneHash[node]
            
            clone = Node(node.val)
            cloneHash[node] = clone

            #iterate over the original node's neighbours preform dfs over them to get the copied neighbour node not the original neighbour node 
            for neighbour in node.neighbors:
                #dfs responsible for creating the clone
                #dfs also responsible for creating the copied neighbours 
                # dfs on the neighbours in order to 1. get the cloned neighbour and 2. get the neighbours of the neighbours
                clone.neighbors.append(dfs(neighbour))
            
            return clone


        return dfs(node)
           

        