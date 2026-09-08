class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0]) 
        #1: Capture unsurrounded regions O -> K (need dfs)
        #2: Capture surrounded regions O -> X (nested for-loops)
        #3: Uncapture unsurrounded regions K -> O (nested for-loops)

        def capture(r, c):
            if (r < 0 or c < 0 or r == rows 
            or c == cols or board[r][c] != 'O'):
                return
            board[r][c] = 'K'
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r + 1, c)
            capture(r, c - 1)
        
        #1
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and 
                (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)
        
        #2:
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        #3
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'K':
                    board[r][c] = 'O'
