class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                curr_sqr = (i // 3) * 3 + (j // 3)
                if curr == '.':
                    continue
            
                if curr in rows[i] or curr in columns[j] or curr in squares[curr_sqr]:
                    return False
                rows[i].add(curr)
                columns[j].add(curr)
                squares[curr_sqr].add(curr)
        
        return True

                