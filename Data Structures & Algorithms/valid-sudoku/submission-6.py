"""
For every digit, check row/col/subbox for dups
return true if no dups found

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def validRow(r):
            seen = set()
            for i in range(ROWS):
                if board[r][i] == ".":
                    continue
                if board[r][i] in seen:
                    return False
                seen.add(board[r][i])
            return True
        
        def validCol(c):
            seen = set()
            for i in range(COLS):
                if board[i][c] == ".":
                    continue
                if board[i][c] in seen:
                    return False
                seen.add(board[i][c])
            return True
        
        def validSubBox(r,c):
            startingRow = (r // 3) * 3
            startingCol = (c // 3) * 3
            seen = set()
            for i in range(startingRow, startingRow + 3):
                for j in range(startingCol, startingCol + 3):
                    if board[i][j] == ".":
                        continue                    
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if not validRow(r) or not validCol(c) or not validSubBox(r,c):
                    return False
        
        return True
        