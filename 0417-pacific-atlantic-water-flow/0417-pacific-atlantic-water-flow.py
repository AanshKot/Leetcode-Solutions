class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #background
        directions = [[1,0],[-1,0],[0,1],[0,-1]] #down up right left
        maxRows = len(heights)
        maxCols = len(heights[0])
        res = []
        pac = set()
        atl = set()    

        def dfs(r, c, visit, prevHeight):
            if (
                (r,c) in visit or
                r not in range(maxRows) or
                c not in range(maxCols) or 
                heights[r][c] < prevHeight #only allowed to traverse from ocean to other ocean if tile height is greater than prevHeight
            ):
                return
            
            visit.add((r,c))

            for direct in directions:
                newRow, newCol = r + direct[0], c + direct[1]
                dfs(newRow, newCol, visit, heights[r][c])


        #first and last row
        for c in range(maxCols):
            #first row means the pacific ocean
            #visit this position and see every other position it can reach
            dfs(0,c, pac, heights[0][c])

            #last row means atlantic ocean
            dfs(maxRows - 1, c, atl, heights[maxRows-1][c])

            #first and last col 
            for r in range(maxRows):
                # every position in the leftmost col (PACIFIC start tiles)
                dfs(r, 0, pac, heights[r][0])

                # every position in the rightmost col (ATLANTIC start tiles)
                dfs(r, maxCols -1, atl, heights[r][maxCols - 1])
        

        for r in range(maxRows):
            for c in range(maxCols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res