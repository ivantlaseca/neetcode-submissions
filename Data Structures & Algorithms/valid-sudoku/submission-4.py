"""
For every number, check row/cols for duplicates
For every sub-box, check neighbors for duplicates



T/S: O(n^2)

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def invalidRow(r):
            seen = set()
            for i in range(9):
                if board[r][i] == ".":
                    continue
                if board[r][i] in seen:
                    return True
                seen.add(board[r][i])
            return False
                
        def invalidColumn(c):
            seen = set()
            for i in range(9):
                if board[i][c] == ".":
                    continue
                if board[i][c] in seen:
                    return True
                seen.add(board[i][c])
            return False
        
        def invalidSubBox(r,c):
            seen = set()
            # Calculate the top-left cell of the 3x3 sub-box
            start_row = (r // 3) * 3
            start_col = (c // 3) * 3
            
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return True
                    seen.add(board[i][j])
            return False
                
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if invalidRow(r) or invalidColumn(c) or invalidSubBox(r,c):
                    return False

        return True
            
        