class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # constants
        maxRows = len(grid)
        maxCols = len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        # visited set
        visited = set()

        maxArea = 0

        def dfs(landTileRow, landTileCol):
            area = 1
            #explore the tiles neighbours
            for direct in directions:
                dR = direct[0]
                dC = direct[1]

                newRow = landTileRow + dR
                newCol = landTileCol + dC

                if (
                    newRow in range(maxRows) and 
                    newCol in range(maxCols) and 
                    (newRow, newCol) not in visited and
                    grid[newRow][newCol] == 1
                ):
                    visited.add((newRow,newCol))
                    area += dfs(newRow, newCol)
            
            return area

        

        for row in range(maxRows):
            for col in range(maxCols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    visited.add((row,col))
                    maxArea = max(maxArea, dfs(row,col))
        
        return maxArea



        