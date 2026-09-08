class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # print(f'first {mid}')
                left = mid + 1
            else:
                right = mid
                # print(f'second {mid}')
        return nums[left]