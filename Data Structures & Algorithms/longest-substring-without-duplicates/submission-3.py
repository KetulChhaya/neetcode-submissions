class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        hashset = set()
        max_ = 0
        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                max_ = max(max_, right - left + 1)
            else:
                while s[left] != s[right]:
                    hashset.remove(s[left])
                    left += 1
                left += 1
            right += 1
        return max_

