class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #first construct the adjacency list representation of the graph
        adjList = {}
        for course in range(numCourses):
            adjList[course] = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        visited = set()
        path = dict() #represents valid ordering of courses 
        print(adjList)
        
        def dfs(course):
            if course in visited:
                return False
            
            if adjList[course] == []:
                #add course to path if no preReq required or all preReq is completed
                path[course] = True
                print(path)
                return True
            
            visited.add(course)

            for preReq in adjList[course]:
                #if cycle detected
                if not dfs(preReq):
                    return False
            #remove this course from the visited set to allow other course-preReq paths to visit it
            visited.remove(course)
            adjList[course] = []
            path[course] = True
            return True

        # run this DFS check for every single course in the case of an unconnected graph
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return list(path.keys())


