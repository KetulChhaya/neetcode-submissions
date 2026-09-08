class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        t, b = 0, r - 1

        while t <= b:
            m = t + (b-t)//2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                break
            
        if not (t <= b):
            return False
        
        l, r = 0, c - 1
        row = t + (b-t) // 2
        while l <= r:
            m = l + (r - l)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False