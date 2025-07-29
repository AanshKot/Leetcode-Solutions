class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}

        # number of nodes in connected undirected graph with no cycles is equal to number of edges + 1
        N = len(edges) #since redundant edge is added number of nodes is equal to number of edges
        
        #our redundant edge is found when our group representative is the same for both the tail and head nodes in an edge
        
        #our initial groups will be the individual nodes, with themselves representing the "group" 
        #graph is 1 indexed
        representatives = []
        for i in range(N+1):
            representatives.append(i)
        
        # this is how we merge our two groups and keep track of group size
        rank = [1] * (N+1)

        def findRep(node):
            #when do we know when to stop traversing?
            #when the node is its group representative
            #when the node is not its group representative we want to continue traversing
            
            groupRep = representatives[node]
            if(node != groupRep):
                groupRep = findRep(representatives[node])

            return groupRep

        def union(node1, node2):
            rep1 = findRep(node1)
            rep2 = findRep(node2)
            
            #if the nodes have the same parent
            if(rep1 == rep2):
                return False
            
            #merge the two groups
            if(rank[rep1] < rank[rep2]):
                representatives[rep1] = rep2
                rank[rep2] += rank[rep1]
            else:
                representatives[rep2] = rep1
                rank[rep1] += rank[rep2]

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
            
            








        