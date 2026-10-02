class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]

        def explore(i ,j, idx, vis):
            if idx == len(word):
                return True
            if i<0 or j<0 or i==m or j==n:
                return False
            if vis[i][j]==1:
                return False
            if board[i][j]!=word[idx]:
                return False
            vis[i][j]=1
            if explore(i-1, j, idx+1, vis) or explore(i+1, j, idx+1, vis) or explore(i, j-1, idx+1, vis) or explore(i, j+1, idx+1, vis):
                return True
            vis[i][j]=0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if explore(i, j, 0, vis):
                        return True
        
        return False

                
        