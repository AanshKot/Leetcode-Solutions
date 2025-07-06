class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid[0]) == 0:
            return 0

        #background
        visited = set()

        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        def bfs(row,col): 
            q = deque()
            # if no diagonal connections (Which is the case)
            directions = {'bottom': [0,1], 'right': [1,0], 'top': [-1, 0], 'left': [0, -1]}

            q.append((row,col))
            visited.add((row,col))

            while len(q) > 0:
                curRow, curCol = q.popleft()

                # if the node is a 1 and hasn't been visited
                # increase the number of islands
                # add the nodes unvisited neighbours to the queue
                # only if they are in bounds
                # mark as visited
                    
                for direction in directions:
                    newRow = curRow + directions[direction][0]
                    newCol = curCol + directions[direction][1]

                    if(newRow in range(rows) 
                        and newCol in range(cols) 
                        and (newRow, newCol) not in visited
                        and grid[newRow][newCol] == '1'
                    ):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))

        #bfs on each node that hasn't been visited
        #if the bfs discovers other '1's in the grid that haven't been visited
        # it means previous BFS attempts didn't connect to this tile
        # as such it is a new island
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    numIslands += 1
        return numIslands

                    
                    




                    
                        

