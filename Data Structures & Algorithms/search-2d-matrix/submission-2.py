class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][-1] < target:
                top = row + 1
            
            elif matrix[row][0] > target:
                bot = row - 1
            
            else: 
                break

            if not (top <= bot):
                return False
        

        curr = (top + bot) // 2
        l,r = 0, cols - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[curr][mid]
            if val == target:
                return True
            
            elif val < target:
                l = mid + 1
            
            else:
                r = mid - 1

        return False