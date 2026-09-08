class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                box_id = (r//3, c//3)
                if (val in row[r] or val in col[c] or val in box[box_id]):
                    return False
                row[r].add(val)
                col[c].add(val)
                box[box_id].add(val)
        # print(box)
        # print(row)
        # print(col)
        return True
                