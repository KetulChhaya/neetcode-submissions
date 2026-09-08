
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        while maxHeap:
            if len(maxHeap) > 1:
                x = abs(heapq.heappop(maxHeap))
                y = abs(heapq.heappop(maxHeap))
                if x != y:
                    diff = abs(x-y)
                    heapq.heappush(maxHeap, -diff)
            else:
                return abs(maxHeap[0])
        return abs(maxHeap[0]) if maxHeap else 0
