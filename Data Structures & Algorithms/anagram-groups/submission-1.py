class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            wordstr = [0] * 26
            for c in s:
                wordstr[ord(c) - ord('a')] += 1
            hmap[str(wordstr)].append(s)
        return list(hmap.values())