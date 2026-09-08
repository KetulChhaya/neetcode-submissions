class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # visit = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        maxArea = 0

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0):
                return 0
            # visit.add((r, c))
            grid[r][c] = 0
            return (1 + dfs(r-1, c) + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1))



        for r in range(ROWS):
            for c in range(COLS):
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
