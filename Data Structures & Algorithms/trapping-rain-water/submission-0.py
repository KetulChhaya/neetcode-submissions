class Solution:
    def trap(self, heights: List[int]) -> int:
        if(not heights or len(heights) < 3): return 0
        n = len(heights)
        leftMax, rightMax = [0] * n, [0] * n
        leftMax[0] = heights[0]
        for i in range(1, len(heights)):
            leftMax[i] = (max(leftMax[i-1], heights[i]))
        
        rightMax[n-1] = heights[n-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = (max(rightMax[i+1], heights[i]))
       
        waterCount = 0
        for i in range(n):
            waterCount += min(rightMax[i],leftMax[i]) - heights[i]

        return waterCount


