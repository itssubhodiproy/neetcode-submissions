class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        
        for i in range (len(board)):
            seen = set()
            for j in range (len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        # check cols
        for i in range (len(board)):
            seen = set()
            for j in range (len(board[i])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        # store all possible top-left in an array and start from there
        top_lefts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for top_left in top_lefts:
            seen = set()
            for i in range (top_left[0], top_left[0]+3):
                for j in range (top_left[1], top_left[1]+3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        # we haven't find any duplicate in all 3 logics - so return true
        return True