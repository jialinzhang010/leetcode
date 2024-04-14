class MedianFinder:

    def __init__(self):
        self.smaller = []   #maxHeap
        self.larger = []    #minHeap
        heapify(self.smaller)
        heapify(self.larger)

    def addNum(self, num: int) -> None:
        # 总是尝试先把num放到大顶堆里，再把大顶堆的最大值放到小顶堆里。
        # 如果小顶堆的长度大于大顶堆了，则把小顶堆的最小值放到大顶堆里。
        heappush(self.smaller, -num)
        heappush(self.larger, -heappop(self.smaller))  #把大顶堆的最大值放到小顶堆
        if len(self.smaller) < len(self.larger):
            heappush(self.smaller, -heappop(self.larger))  #保持大顶堆比小顶堆多至多一个元素

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        else:
            return (self.larger[0] - self.smaller[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()