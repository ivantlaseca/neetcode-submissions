"""
Algo:
Run a scan on each digit in our matrix. Scan the row, col, and sub-box for duplicates. If found, return False.
Return True if no dups found.

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        def validRow(r):
            seen = set()
            for i in range(N):
                if board[r][i] == ".":
                    continue
                if board[r][i] in seen:
                    return False
                seen.add(board[r][i])
            return True
        
        def validCol(c):
            seen = set()
            for i in range(N):
                if board[i][c] == ".":
                    continue
                if board[i][c] in seen:
                    return False
                seen.add(board[i][c])
            return True

        def validBox(r,c):
            seen = set()
            start_row = (r // 3) * 3
            start_col = (c // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True


        for r in range(N):
            for c in range(N): 
                if board[r][c] == ".":
                    continue
                if not validRow(r) or not validCol(c) or not validBox(r, c):
                    return False
        return True

        