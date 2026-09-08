class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        sizeRank = [1] * n
                
        def find(n1):
            curr = n1
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if sizeRank[p1] > sizeRank[p2]:
                parent[p2] = p1
                sizeRank[p1] += sizeRank[p2]
            else:
                parent[p1] = p2
                sizeRank[p2] += sizeRank[p1]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
        
        