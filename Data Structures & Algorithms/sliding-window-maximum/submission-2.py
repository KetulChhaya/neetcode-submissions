class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        left = right = 0
        res = []
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if q[0] < left:
                q.popleft()
            
            if (right - left + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        
        return res