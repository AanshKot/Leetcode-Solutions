class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        #directed graph in the form of an adjacency list
        for i in range(numCourses):
            adjList[i] = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        
        #dfs with visited and path
        #dfs returns False if it detects a cycle
        visited = set() #if already visited node return False cycle detected
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
           
            
            visiting.add(course)

            for preReq in adjList[course]:
                if not dfs(preReq):
                    return False

            adjList[course] = [] #viable to take a course even with its prereqs
            visited.add(course) #only mark courses as visited after successful traversal of all neighbours without cycle
            visiting.remove(course)
            return True


        #graph is directed, passing a new visiting set each time would mean that not aware of cycle
        # 0 -> 1 , 1 -> 0 are different bfs with a cycle
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



            



        