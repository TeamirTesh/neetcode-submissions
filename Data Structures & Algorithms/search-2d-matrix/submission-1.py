class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curr = 0

        while curr < len(matrix) and matrix[curr][-1] < target:
            curr += 1
        
        if curr == len(matrix):
            return False

        l,r = 0, len(matrix[0])

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