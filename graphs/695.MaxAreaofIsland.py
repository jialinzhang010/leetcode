class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = []
        def helper(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return

            area[0] += 1
            grid[i][j] = 0
            helper(i + 1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = [0]
                    helper(i, j)
                    ans.append(area[0])
                    print(area)
        return max(ans) if ans else 0