class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        # background
        visited = set()
        maxRows = len(grid)
        maxCols = len(grid[0])
        maxArea = 0
        directions = [[-1,0], [1,0], [0, -1], [0, 1]]

        def dfs(tileX, tileY):
            # base case
            if grid[tileX][tileY] == 0 or (tileX, tileY) in visited:
                return 0 

            #add current tile to visited set
            visited.add((tileX, tileY))
            area = 1

            # dfs for every tile in every possible direction
            # only dfs IF the following conditions are met
            # 1. tile within bounds
            # 2. if the tile is a water tile
            
            for direct in directions:
                newTileX = tileX + direct[0]
                newTileY = tileY + direct[1]

                if(
                    newTileX in range(maxRows) and
                    newTileY in range(maxCols) and
                    grid[newTileX][newTileY] == 1
                ):
                    area += dfs(newTileX, newTileY)

            return area
        
        for x in range(maxRows):
            for y in range(maxCols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    maxArea = max(maxArea, dfs(x,y))

        return maxArea


        