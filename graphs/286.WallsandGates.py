class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        
        R, C = len(rooms), len(rooms[0])
        q = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dx < R and 0 <= c + dy < C and rooms[r + dx][c + dy] > rooms[r][c]:
                    rooms[r + dx][c + dy] = rooms[r][c] + 1
                    q.append((r + dx, c + dy))
                    
        