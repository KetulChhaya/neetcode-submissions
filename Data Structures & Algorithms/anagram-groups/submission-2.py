class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for ch in word:
                arr[ord(ch) - ord('a')] += 1
            hmap[str(arr)].append(word)
        return list(hmap.values())