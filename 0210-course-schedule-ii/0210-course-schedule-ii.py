class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #construct adjacency list
        adjList = {}

        for course in range(numCourses):
            adjList[course] = []

        for course, preReq in prerequisites:
            #source node (Course) has a prereq (sink node)
            adjList[course].append(preReq)
        
        # visited is the set of nodes we have traversed in the current  recursive call stack
        visited = set()
        # represents the set of nodes whose neighbours we have traveled and already seen
        # this set is for constructing our course schedule
        seen = []
        def dfs(course):
            #cyclic graph
            if course in visited:
                return False
            if course in seen:
                return True
    
            #course has no prereqs
            if adjList[course] == []:
                seen.append(course)
                return True

            visited.add(course)

            for preReq in adjList[course]:
                if not dfs(preReq):
                    return False

            #remove course from visited we have traveled to all its neighbours and it is a clean path
            #this node can also be the terminating node/ or a sink node in another path 
            #in other words this course can be the prereq of another
            visited.remove(course)
            #traversed this course completely and completed its pre reqs
            seen.append(course) 
            # already checked course can now set its pre reqs to none/empty
            adjList[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return seen
            

