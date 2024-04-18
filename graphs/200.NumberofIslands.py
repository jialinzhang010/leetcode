class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        def helper(i, j, ans):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # mark grid[i][j] as visited
            grid[i][j] = '0'
            helper(i + 1, j, ans)
            helper(i, j + 1, ans)
            helper(i - 1, j, ans)
            helper(i, j - 1, ans)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 把与该1连接的所有1都变成0
                    helper(i, j, ans)
                    ans += 1
        return ans