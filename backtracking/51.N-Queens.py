class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        ans = []
        board = [["."] * n for i in range(n)]
    
        def helper(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r -c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                helper(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        helper(0)
        return ans