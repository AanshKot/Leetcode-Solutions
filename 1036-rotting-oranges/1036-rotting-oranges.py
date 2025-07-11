class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        freshOranges = 0

        maxRows = len(grid)
        maxCols = len(grid[0])
        # up down left right
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        # background
        # count number of fresh oranges
        # append rotten oranges to bfs

        for r in range(maxRows):
            for c in range(maxCols):
                if grid[r][c] == 1:
                    freshOranges += 1

                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and freshOranges > 0:
            curLevelLength = len(q)
            # pop rotten oranges at the same time
            for i in range(curLevelLength):
                rowRotten, colRotten = q.popleft()

                for direct in directions:
                    newRow = rowRotten + direct[0]
                    newCol = colRotten + direct[1]

                    #if fresh orange and in bounds
                    # infect the orange
                    # pass it to the queue
                    if(
                        newRow in range(maxRows) and
                        newCol in range(maxCols) and
                        grid[newRow][newCol] == 1
                    ):
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
                        freshOranges -= 1
    
            # after traversing level and simulateously infecting fresh oranges from infected oranges
            time += 1

        #if no fresh oranges successfully infected entire grid
        if freshOranges == 0: 
            return time
        
        return -1


