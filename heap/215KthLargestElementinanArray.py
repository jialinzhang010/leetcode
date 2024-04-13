class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        
        while k > 1:
            heappop(heap)
            k -= 1
        
        return -heap[0]