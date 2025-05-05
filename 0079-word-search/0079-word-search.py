class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows = len(board) 
        cols = len(board[0]) 
        
        path = set()

        def dfs(r, c, i):
            # i is the current character in our target word, if i ever reaches the last position of the word we found the word
            if i == len(word):
                return True

            # what if we go out of bounds bounds up: (r < 0),  down: (r >= rows), left: c < 0, right: c >= cols
            # word[i] != board[r][c] current tile doesn't match word at index i
            # if we already visited (r,c)
            if (r < 0 or c < 0 or 
            r >= rows or c >= cols 
            or word[i] != board[r][c] or 
            (r,c) in path ):
                return False

            path.add((r,c))

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            #cleanup
            # returning from function call therefore no longer visiting tile in our path
            path.remove((r,c))

            return res

        # check every possible entry in the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0): return True
        return False