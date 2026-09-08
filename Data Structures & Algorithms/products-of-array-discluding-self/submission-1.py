class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productTotal = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                productTotal *= num
            else:
                zeroCount += 1
            
        if zeroCount > 1:
            return [0] * len(nums)

        for i, num in enumerate(nums):
            if zeroCount > 0:
                nums[i] = 0 if num else productTotal
            else:
                nums[i] = productTotal // num
        return nums