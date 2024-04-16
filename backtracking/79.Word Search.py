class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, k):
            if len(word) == k:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[k] != board[i][j] or (i, j) in path:
                return False
            
            path.add((i, j))
            ans = helper(i + 1, j, k + 1) or helper(i, j + 1, k + 1) or helper(i - 1, j, k + 1) or helper(i, j - 1, k + 1)
            path.remove((i, j))
            return ans
        path = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False