class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            max_path = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                currX, currY = i + dx, j + dy
                if currX < 0 or currX >= len(matrix) or currY < 0 or currY >= len(matrix[0]) \
                or matrix[currX][currY] <= matrix[i][j]:
                    continue
                else:
                    currLength = 1 + dfs(currX, currY)
                    max_path = max(max_path, currLength)
            memo[i][j] = max_path
            return max_path
        max_inc_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_inc_path = max(max_inc_path, dfs(i, j))
        return max_inc_path
