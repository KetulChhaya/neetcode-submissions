class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + (str(len(string))+'#' + string)
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            lengthstr = ""
            while s[i] != '#':
                lengthstr += s[i]
                i += 1
            length = int(lengthstr)
            res.append(s[i+1: i+length+1])
            i = i + length + 1
        return res
            
           