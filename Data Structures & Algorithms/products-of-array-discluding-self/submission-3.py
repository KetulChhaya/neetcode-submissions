class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefixStart = 1
        for i in range(len(nums)):
            prefix[i] = prefixStart
            prefixStart = prefixStart * nums[i]
        
        suffix = [1] * len(nums)
        suffixStart = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffixStart
            suffixStart = suffixStart * nums[i]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
        
            