class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows=[[] for _ in range(9)]
    cols=[[] for _ in range(9)]
    box= [[list() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            if num in rows[r] or num in cols[c] or num in box[r//3][c//3]:
                return False
            rows[r].append(num)
            cols[c].append(num)
            box[r//3][c//3].append(num)
    return True