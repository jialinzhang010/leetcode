class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = Counter(tasks)
        maxHeap = []
        for value in t.values():
            maxHeap.append(-value)
        heapify(maxHeap)
        queue = []
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                remaining_cnt = 1 + heappop(maxHeap)
                if remaining_cnt:
                    next_available_t = time + n
                    queue.append([remaining_cnt, next_available_t])
            if queue and queue[0][1] == time:
                heappush(maxHeap, queue.pop(0)[0])
        
        return time
