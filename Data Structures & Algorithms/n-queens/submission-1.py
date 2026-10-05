class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        col_set, pos_diag, neg_diag = set(), set(), set()

        def can_place(row, col):
            if (col in col_set or row+col in pos_diag or row-col in neg_diag):
                return False
            return True

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if not can_place(row, col):
                    continue
                    
                else:
                    board[row][col] = "Q"
                    col_set.add(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)

                    backtrack(row+1)

                    board[row][col] = "."
                    col_set.remove(col)
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)

        backtrack(0)
        return ans
