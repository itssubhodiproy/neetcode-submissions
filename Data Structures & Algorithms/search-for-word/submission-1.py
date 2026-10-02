class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def backtrack(row, col, index):
            # Entire word matched
            if index == len(word):
                return True

            # Out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # Can't reuse a cell in the current path
            if visited[row][col]:
                return False

            # Current character doesn't match
            if board[row][col] != word[index]:
                return False

            # Choose
            visited[row][col] = True

            # Explore all four neighbors
            found = (
                backtrack(row - 1, col, index + 1) or
                backtrack(row + 1, col, index + 1) or
                backtrack(row, col - 1, index + 1) or
                backtrack(row, col + 1, index + 1)
            )

            # Backtrack
            visited[row][col] = False

            return found

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    # we got a possible candidate - look for the word
                    if backtrack(row, col, 0):
                        return True

        return False