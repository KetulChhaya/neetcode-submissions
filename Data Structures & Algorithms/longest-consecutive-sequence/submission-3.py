class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_ = 0
        for n in hashset:
            if n - 1 not in hashset:
                cnt = 1
                while n + cnt in hashset:
                    cnt += 1
                max_ = max(max_, cnt)
        return max_



        # hashset = set()
        # start = []
        # for n in nums:
        #     hashset.add(n)
        # for n in hashset:
        #     if n-1 not in hashset:
        #         start.append(n)
        # max_ = 0
        # for n in start:
        #     cnt = 1
        #     while n + 1 in hashset:
        #         cnt += 1
        #         n+=1
        #     max_ = max(max_, cnt)
        # return max_
