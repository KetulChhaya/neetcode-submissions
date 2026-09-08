class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {} #key: sorted characters, value: keyword original
        for string in strs:
            arr = [0]*26
            for c in string:
                arr[ord(c) - ord('a')] += 1
            key = tuple(arr)
            if key in hmap:
                hmap[key].append(string)
            else:
                hmap[key] = [string]
        return list(hmap.values())