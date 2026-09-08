class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[right] + nums[left] == target:
                return [left + 1, right + 1]
            elif nums[right] + nums[left] < target:
                left += 1
            else:
                right -= 1
            
        return None

                    