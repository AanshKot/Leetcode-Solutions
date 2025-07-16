class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create directed graph in the form of an adjacency list
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)

        visited = set()
        def dfs(course):
            if course in visited:
                return False #cycle detected unable to take course schedule

            if preMap[course] == []:
                return True
            
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return  False
        
            # if we exit the for loop inside dfs we know that the course is a good node without cycles
            # we remove it from visited so other paths can successfully revisit it
            # we can visit the node twice without it being a cycle due to it terminating multiple paths
            visited.remove(course)
            preMap[course] = []

            return True

        # if we recieve a disconnected graph i.e. 1 -> 2 and 3 -> 4
        for course in range(numCourses):
            #if cycle detected in DFS we know we cant take this course schedule
            if not dfs(course):
                return False
        return True




            



        