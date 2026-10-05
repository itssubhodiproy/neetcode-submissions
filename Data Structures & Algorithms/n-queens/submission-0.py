class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        col_set = set()

        def can_place(row, col):
            # upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in col_set:
                    continue
                
                if not can_place(row, col):
                    continue
                    
                else:
                    board[row][col] = "Q"
                    col_set.add(col)

                    backtrack(row+1)

                    board[row][col] = "."
                    col_set.remove(col)

        backtrack(0)
        return ans
