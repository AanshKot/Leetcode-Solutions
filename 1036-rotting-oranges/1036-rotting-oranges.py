class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # constants
        maxRows = len(grid)
        maxCols = len(grid[0])
        directions = [[-1,0], [1,0], [0, -1], [0,1]]


        # BFS
        q = deque()
        numRipeOranges = 0
        visited = set() # this set stores the positions that have already been traversed

        # first pass
        for row in range(maxRows):
            for col in range(maxCols):
                if grid[row][col] == 1:
                    numRipeOranges += 1
                
                elif grid[row][col] == 2:
                    q.append((row,col))
                    visited.add((row, col))

        if numRipeOranges == 0:
            return 0

        # result
        minTime = 0

        # second pass is our actual BFS
        while q and numRipeOranges > 0:
            lengthLevel = len(q)
            print(q)
            for i in range(lengthLevel):
                rotOrangeRow, rotOrangeCol = q.popleft()
                visited.add((rotOrangeRow, rotOrangeCol))
                #from this rotting orange we want to see what ripe oranges we can infect
                for dRow, dCol in directions:
                    newRow, newCol = rotOrangeRow + dRow, rotOrangeCol + dCol
                    
                    if(
                        newRow in range(maxRows) and 
                        newCol in range(maxCols) and
                        (newRow, newCol) not in visited and
                        grid[newRow][newCol] == 1
                    ):
                        grid[newRow][newCol] = 2
                        q.append((newRow,newCol))
                        # add to visited set as we have reached it from a rotting orange and don't want other rotting oranges to traverse on an already infected ripe orange
                        visited.add((newRow,newCol))
                        numRipeOranges -= 1
                
            minTime += 1 # a level represents the rotting oranges infected at time t 

        if numRipeOranges > 0:
            #infection failed
            return -1
        
        return minTime




        



        