class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        
        ans = []
        for i in range(len(points)):
            heappush(heap, (-self.findDist(points[i][0], points[i][1]), points[i][0], points[i][1]))
        while len(heap) > k:
            heappop(heap)
        while heap:
            curr = heappop(heap)
            ans.append([curr[1], curr[2]])
        return ans
    def findDist(self, x, y):
        return sqrt(x ** 2 + y ** 2)