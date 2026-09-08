class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums): return -1
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        while k > 1:
            if maxHeap:
                heapq.heappop(maxHeap)
                k -= 1
        print(maxHeap)
        return abs(maxHeap[0]) if maxHeap[0] < 0 else -maxHeap[0]
            
       