class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        window = {}
        resLen = float('inf')
        res = ""
        left = 0
        have = 0
        need = len(countT)
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = s[left:right+1]
                a = s[left]
                window[a] -= 1
                if a in countT and window[a] < countT[a]:
                    have -= 1
                left += 1
        return res
            