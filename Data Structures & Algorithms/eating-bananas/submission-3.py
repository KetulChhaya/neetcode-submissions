import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #brute force approach
        # for k in range(1, max(piles) + 1): #ascending / sorted order
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/k)
        #     if hours <= h:
        #         return k

        #optimal approach
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
         

        