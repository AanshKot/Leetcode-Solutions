class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        # define constants
        maxRows = len(heights)
        maxCols = len(heights[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        pacificSet = set()
        atlanticSet = set()
        
        # traverse from pacific to atlantic border
        # traverse from atlantic to pacifice border
        #visited tiles are tiles we can reach from the pacific border and so we add it to the pacificSet
        def dfs(tileRow, tileCol, visited, prevHeight):
           #if the tile is in the pacific or atlantic set already no need to traverse on it
            if (
            tileRow not in range(maxRows) or 
            tileCol not in range(maxCols) or
            (tileRow, tileCol) in visited or 
            heights[tileRow][tileCol] < prevHeight # water can't flow from shorter curr tile to taller border tile
            ):
                return 
            
            visited.add((tileRow, tileCol))

            for direct in directions:
                dRow = direct[0]
                dCol = direct[1]

                newTileRow = tileRow + dRow
                newTileCol = tileCol + dCol

                dfs(newTileRow, newTileCol, visited, heights[tileRow][tileCol]) 

        for row in range(maxRows):
            dfs(row, 0, pacificSet, heights[row][0])
            dfs(row, maxCols - 1, atlanticSet, heights[row][maxCols-1])
        
        for col in range(maxCols):
            dfs(0, col, pacificSet, heights[0][col])
            dfs(maxRows -1, col, atlanticSet, heights[maxRows-1][col])
        
            

        # final part of the function
        for row in range(maxRows):
            for col in range(maxCols):
                if (row,col) in pacificSet and (row,col) in atlanticSet:
                    res.append([row,col])
        
        return res 

        