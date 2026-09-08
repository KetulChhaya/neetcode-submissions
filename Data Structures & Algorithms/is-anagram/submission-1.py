class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1, m2 = defaultdict(list), defaultdict(list)
        for c in s:
            m1[c] = m1.get(c, 0) + 1
        for c in t:
            m2[c] = m2.get(c, 0) + 1
        
        return m1 == m2
            
