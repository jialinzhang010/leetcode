class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap = nums
        self.k = k 

        heapify(self.minHeap)


    def add(self, val: int) -> int:
        heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]

    