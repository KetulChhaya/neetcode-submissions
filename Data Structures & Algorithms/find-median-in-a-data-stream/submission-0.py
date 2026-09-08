class MedianFinder:

    def __init__(self):
        #two heaps: large (minHeap) and small (maxHeap)
        self.small, self.big = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.big and (-1 * self.small[0]) > self.big[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.small) > len(self.big) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.big) > len(self.small) + 1:
            val = heapq.heappop(self.big)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -1 * self.small[0]
        if len(self.big) > len(self.small):
            return self.big[0]
        return ((-1 * self.small[0]) + self.big[0]) / 2