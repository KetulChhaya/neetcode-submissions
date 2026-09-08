class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElems = []
        temp = []
        l=0
        for r in range(len(nums)):
            if (r-l) == k:
                # print(temp)
                maxElems.append(max(temp))
                temp[l] = -1
                l += 1
            temp.append(nums[r])
           
        maxElems.append(max(temp))
        return maxElems