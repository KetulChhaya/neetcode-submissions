class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictmap = {}
        for i in range(len(nums)):
            if target - nums[i] in dictmap:
                return [dictmap[target - nums[i]], i]
            dictmap[nums[i]] = i
        return [0,0]
