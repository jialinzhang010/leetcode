class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def capture(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r - 1, c)
            capture(r, c- 1)
            capture(r + 1, c)
            capture(r, c + 1)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    # 把与border相连的方格全变成“T”
                    capture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
