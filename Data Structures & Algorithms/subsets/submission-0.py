class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #to include the number into existing subset
            subset.append(nums[i])
            dfs(i+1)

            #not to include or remove the number into existing subset
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res