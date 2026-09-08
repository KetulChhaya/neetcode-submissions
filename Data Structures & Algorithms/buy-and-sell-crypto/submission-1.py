class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minVal = float("inf")
        # maxProfit = 0

        # for price in prices:
        #     minVal = min(minVal, price)
        #     maxProfit = max(maxProfit, price - minVal)
        
        # return maxProfit

        ## Other Approach
        l,r = 0, 1
        maxProfit = 0
        while r < len(prices):
            # profitable
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit