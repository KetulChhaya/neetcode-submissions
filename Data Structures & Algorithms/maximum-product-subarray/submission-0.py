class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax * n
            currMax = max(currMax * n, n * currMin, n) # [-1, 8]
            currMin = min(temp, n * currMin, n) #[-1, -8]
            res = max(currMax, res)
        return res