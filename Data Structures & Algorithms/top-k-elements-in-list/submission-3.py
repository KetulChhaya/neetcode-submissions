from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            print(num, freq)
            heapq.heappush(heap, (-freq, num))
        res = []
        while k > 0:
            popped = heapq.heappop(heap)
            res.append(popped[1])
            k -= 1
        return res