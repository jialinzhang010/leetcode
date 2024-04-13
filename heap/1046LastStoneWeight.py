class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_cp = []
        for i in stones:
            stone_cp.append(-i)

        heapify(stone_cp)
        while len(stone_cp) > 1:
            y = heappop(stone_cp)
            x = heappop(stone_cp)
            if x == y:
                continue
            else:
                heappush(stone_cp, y - x)
        return -stone_cp[0] if stone_cp else 0
