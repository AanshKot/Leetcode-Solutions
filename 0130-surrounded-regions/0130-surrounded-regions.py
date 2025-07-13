class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # background
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        maxRows = len(board)
        maxCols = len(board[0])
        # visited set of 0's that can be reached from a border 0
        visited = set()
        q = deque()

        #first traverse the board and to the queue add all border 0's
        for row in range(maxRows):
            if board[row][0] == 'O' and (row,0) not in visited:
                visited.add((row,0))
                q.append((row,0))

            if board[row][maxCols - 1] == 'O' and (row,maxCols-1) not in visited:
                visited.add((row, maxCols - 1))
                q.append((row, maxCols-1))
            
        for col in range(maxCols):
            if board[0][col] == 'O' and (0,col) not in visited:
                visited.add((0,col))
                q.append((0,col))

            if board[maxRows-1][col] =='O' and (maxRows-1, col) not in visited:
                visited.add((maxRows-1,col))
                q.append((maxRows-1, col))
        print(q)

        # start BFS from all our 0s 
        while q:
            lengthLevel = len(q)

            for i in range(lengthLevel):
                curRow, curCol = q.popleft()
                visited.add((curRow, curCol))

                # from this 0 we want to find every other 0 
                for direct in directions:
                    newRow = curRow + direct[0]
                    newCol = curCol + direct[1]

                    if( 
                        newRow in range(maxRows) and
                        newCol in range(maxCols) and 
                        board[newRow][newCol] == "O" and
                        (newRow, newCol) not in visited
                    ):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))

        print(visited)

        # visited reps all the O nodes reachable from a border O node
        for r in range(maxRows):
            for c in range(maxCols):
                if board[r][c] == "O" and (r,c) not in visited:
                    print('hitting this condition')
                    board[r][c] = "X"
                
            