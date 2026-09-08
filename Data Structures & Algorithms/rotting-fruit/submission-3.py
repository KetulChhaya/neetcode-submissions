class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def bfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] == 0):
                return
            grid[r][c] = 2
            q.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r+1, c)
                bfs(r, c-1)
            if q:
             dist += 1
        isPresent = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    isPresent = True
        
        return -1 if (dist == 0 and isPresent) or isPresent else dist