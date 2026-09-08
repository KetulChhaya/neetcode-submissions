class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        res = []
        visit = set() #already considered all the outgoing prerequisited of that curr node
        cycle = set() #is in pipeline, remaining to have a chance of curr node in backtrack
        def dfs(currCrs):
            if currCrs in visit:
                return True
            if currCrs in cycle:
                return False
            cycle.add(currCrs)
            for pre in preMap[currCrs]:
                if not dfs(pre):
                    return False
            cycle.remove(currCrs)
            visit.add(currCrs)
            res.append(currCrs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res