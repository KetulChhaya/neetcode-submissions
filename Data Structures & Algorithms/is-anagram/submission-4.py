class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # m1, m2 = defaultdict(list), defaultdict(list)
        # for i in range(len(s)):
        #     m1[s[i]] = m1.get(s[i], 0) + 1
        #     m2[t[i]] = m2.get(t[i], 0) + 1
        # return m1 == m2

        arr1, arr2 = [0] * 26, [0] * 26
        for i in range(len(s)):
            arr1[ord(s[i]) - ord('a')] += 1
            arr2[ord(t[i]) - ord('a')] += 1
        print(arr1, arr2)
        return arr1 == arr2
            
