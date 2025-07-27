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
        def dfs(course, visiting):
            if course in visiting:
                return False

            if course in visited:
                return True
           
            visited.add(course)
            visiting.add(course)

            for preReq in adjList[course]:
                if not dfs(preReq, visiting):
                    return False

            adjList[course] = [] #viable to take a course even with its prereqs
            visiting.remove(course)
            return True


        #
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True



            



        