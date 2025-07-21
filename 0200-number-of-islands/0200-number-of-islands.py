class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid[0]) == 0:
            return 0

        #Constants:
        maxRows = len(grid)
        maxCols = len(grid[0])
        
        #visited set
        visited = set()

        # number of islands
        numIslands = 0

        # directions R -> L -> U -> D
        directions = [[0,1], [0, -1], [-1, 0], [1,0]]

        def bfs(landTileRow, landTileCol):
            q = deque()

            q.append((landTileRow, landTileCol))

            while q:
                curRow, curCol = q.popleft()

                visited.add((curRow, curCol))

                for dRow, dCol in directions:
                    newRow = curRow + dRow
                    newCol = curCol + dCol

                    # only want to append neighbour if it hits these conditions
                    # 1. is the tile within our grid
                    # 2. is the tile a land tile
                    # 3. has the tile been visited already  

                    if(
                        newRow in range(maxRows) and
                        newCol in range(maxCols) and
                        (newRow,newCol) not in visited and 
                        grid[newRow][newCol] == "1"
                    ):
                        visited.add((newRow, newCol))
                        q.append((newRow,newCol))


        for row in range(maxRows):
            for col in range(maxCols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    numIslands += 1
                    bfs(row, col)
        
        return numIslands




        




                    
                        

