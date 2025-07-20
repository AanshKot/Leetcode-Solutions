class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #1. first establish the array of representives
        representatives = []
        
        # they mention we are given a tree initially ~ undirected graph that is connected and has no cycles
        # in a undirected connected graph without cycles 
        # the number of edges in the graph is equal to the number of nodes - 1 (N-1 edges)
        # but since we added an edge thisg raph now has a cycle and is no longer a tree
        # therefore the number of edges is equal to the number of nodes
        N = len(edges)

        #the nodes are from 1 -> n
        for i in range(N+1):
            representatives.append(i)

        groupSize = [1] * (N+1)

        # two methods that implement union-find
        def findRepresentative(node):
            # want to traverse up the graph-tree to find the node's group representive
            # we know a node is its group's representive if its its own representive 
            # if it isn't its own representive keep traversing up the graph-tree until we find its reprsentive
            rep = representatives[node]
            if(node != rep):
                #flatten the graph-tree by finding the root group rep and setting it to the current node's rep
                representatives[node] = findRepresentative(rep)
                
            # potentially could have updated rep and so cannot return a stale representative
            return representatives[node]

        # pass in edges here to form the groups
        def union(node1, node2):
            # first we want to find the node's group representive
            rep1 = findRepresentative(node1)
            rep2 = findRepresentative(node2)

            # if the two node's representives are the same, we know they are apart of the same group
            # and so the edge we have passed in is the redundant one and causes a cycle
            # Plan A: node2 has already tapped the group representive to join the group, and so is already a part of the group
            # Plan B: at the same time node2 taps a member node (i.e. node1) to join the group as a redundancy plan (but plan A always works out)
            # causing a cycle
            if(rep1 == rep2):
                # note there is some further logic for union-find algo but not required for this problem
                return False
            
            # if the group representives aren't the same
            # the larger group acquires the smaller group
            if(groupSize[rep1] > groupSize[rep2]):
                # increase the size of rep1's group
                # as we have just merged rep2's group into it
                groupSize[rep1] += groupSize[rep2]
                # set the new representitive of node2 to rep1 as the group has been merged
                # note we are setting the representative's representative because its the overall group's representative
                representatives[rep2] = rep1
            else:
                groupSize[rep2] += groupSize[rep1]
                representatives[rep1] = rep2
            
            return True

        #now for every edge we want to start unioning our individual groups 
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        








        