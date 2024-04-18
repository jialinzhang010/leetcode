class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        ans = 0
        
        while q:
            rotten = False
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    currR = r + dx
                    currC = c + dy
                    if 0 <= currR < len(grid) and 0 <= currC < len(grid[0]):
                        if grid[currR][currC] == 0:
                            continue
                        if grid[currR][currC] == 1:
                            grid[currR][currC] = 2
                            q.append((currR, currC))
                            rotten = True
            if rotten:
                ans += 1
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return ans