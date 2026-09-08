class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left, right = 0, 0
        # hashset = set()
        # max_ = 0
        # while right < len(s):
        #     if s[right] not in hashset:
        #         hashset.add(s[right])
        #         max_ = max(max_, right - left + 1)
        #     else:
        #         while s[left] != s[right]:
        #             hashset.remove(s[left])
        #             left += 1
        #         left += 1
        #     right += 1
        # return max_

        #Optimal Approach (direct jump of left and no iteration)
        left = 0
        max_ = 0
        charIndex = {}
        for right in range(len(s)):
            if s[right] in charIndex and charIndex[s[right]] >= left:
                left = charIndex[s[right]] + 1
            charIndex[s[right]] = right
            max_ = max(max_, right - left + 1)
        return max_

