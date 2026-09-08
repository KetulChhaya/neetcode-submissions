class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':  # Fix: check character, not index
                j += 1
            length = int(s[i:j])  # Length parsing AFTER we found '#'
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length  # Move i to next encoded string
        return res
