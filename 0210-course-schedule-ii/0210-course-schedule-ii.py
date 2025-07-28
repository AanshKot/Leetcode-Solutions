class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #rep graph as adj list
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)
        
        # dfs with visiting courses representing courses in recursive call stack
        res = []
        visited = set()
        visiting = set()

        def dfs(course):
            #this means its neighbours have already been traversed
            if course in visited:
                return True
            if course in visiting:
                return False

            visiting.add(course)

            for preReq in adjList[course]:
                if not dfs(preReq):
                    return False

            res.append(course)
            visited.add(course) #only mark course as successfully traversed if no cycle detected with neighbours
            visiting.remove(course)
            return True



        for course in range(numCourses):
            if not dfs(course):
                return []
        return res





