class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # bottom row always contains greater numbers in its sub-array
        top, bottom = 0, rows - 1

        # binary search rows to get to correctish row
        while top <= bottom:
            midPoint = (top + bottom) // 2

            #leftmost entry in row is greater than target, move bottom up
            if(matrix[midPoint][0] > target):
                bottom = midPoint - 1
            
            elif(matrix[midPoint][cols - 1] < target):
                top = midPoint + 1
            else:
                break
        
        # the row to search on is the midpoint now
        row = (top + bottom) // 2

        low, high = 0, cols - 1

        #once found row, perform regular binary search
        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True
        
        return False



        