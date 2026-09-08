class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findTarget(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        deflection = left
        # left, right = 0, len(nums) - 1
        if deflection == 0 or target < nums[0]:
            return findTarget(deflection, len(nums) - 1)
        else:
            return findTarget(0, deflection - 1)
        # if nums[left]<=target<=nums[deflection]:
        #     return findTarget(0, deflection - 1)
        # else:
        #     return findTarget(deflection, right)