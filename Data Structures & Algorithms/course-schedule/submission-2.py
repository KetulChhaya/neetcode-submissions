class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, requirement in prerequisites:
            preMap[course].append(requirement)
        
        visit = set() #all courses along the curr dfs path
        def dfs(currCourse):
            if currCourse in visit:
                return False
            if preMap[currCourse] == []:
                return True

            visit.add(currCourse)
            for pre in preMap[currCourse]:
                if not dfs(pre): return False
            visit.remove(currCourse)
            preMap[currCourse] = []
            return True
        
        for crs in range(numCourses): #this is only present to check for all the nodes in case of disconnected graph nodes
            if not dfs(crs): return False
        return True