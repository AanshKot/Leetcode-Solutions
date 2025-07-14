class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first iteration
        graphAdjList = {}

        for i in range(numCourses):
            graphAdjList[i] = set()


        for courseDependency in prerequisites:
            graphAdjList[courseDependency[0]].add(courseDependency[1])
        
        #we have adjacency list how do we detect a cycle
        recursionStack = [False] * numCourses
        visited = [False] * numCourses
        
        # graph has a cycle if there is a node that has an edge to an ancestor in the DFS recursive stack
        def detectCycleDFS(adjacencyList, curNode, visited, recursionStack):
            if recursionStack[curNode]:
                return True
            
            if visited[curNode]: #if the node has already been visited and not in the recursion stack 
               return False

            visited[curNode] = True
            recursionStack[curNode] = True

            #check if every node 
            for node in adjacencyList[curNode]:
                if(detectCycleDFS(adjacencyList, node, visited, recursionStack)):
                    return True
            
            recursionStack[curNode] = False
            return False
        
        for i in graphAdjList:
            if detectCycleDFS(graphAdjList, i, visited, recursionStack):
                return False

        return True
            
          



        