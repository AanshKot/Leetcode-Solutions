class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # this represents the bottom row

        # go through all rows
        for i in range(m-1):
            newRow = [1] * n #this new row is above the old row

            # last value in every row is always going to be 1, rightmost value in every row is going to be 1 skip computing it
            # column index within the current row
            for j in range(n - 2, -1, -1): #iterate through the current row
                #newRow[j] = value to the right of the current entry + value below the current entry
                #val to the right of cur entry
                right = newRow[j + 1]
                #old row (row we computed before) val below the current entry
                below = row[j]
                newRow[j] = right + below
            row = newRow # row is going to be set to the row above it
        
        return row[0]
        