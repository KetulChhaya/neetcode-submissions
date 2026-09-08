class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_ = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_= max(area, max_)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_