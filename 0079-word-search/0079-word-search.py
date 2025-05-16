class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        visited = set()
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, r, c):
            # our pointer has reached the end of the word, traveled full word, it exists in board
            if i >= len(word):
                return True

            
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) # reached boundary conditions
                or (r, c) in visited  # if our current tile has already been visited
                or board[r][c] != word[i]):  # if the tile doesn't match where we are currently at in the word
                return False

            visited.add((r, c))
            res =  (dfs(i + 1, r - 1, c)  # up  
                    or dfs(i + 1, r + 1, c)  # down 
                    or dfs(i + 1, r, c - 1)  # left
                    or dfs(i + 1, r, c + 1))  # right

            #cleanup
            #returning from function call therenofe no longer visiting tile in our path
            visited.remove((r,c))
            
            return res

        #have to do check for every entry in board
        for r in range(rows):
            for c in range(cols):
                if (dfs(0,r,c)): return True

        return False
