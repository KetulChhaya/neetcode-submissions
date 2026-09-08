class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCount = 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                total = total * n
        
        if zeroCount > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if zeroCount > 0:
                nums[i] = 0 if nums[i] != 0 else total
            else:
                nums[i] = total // nums[i]
        return nums