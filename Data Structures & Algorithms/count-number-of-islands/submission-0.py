class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        m, n, ans = len(grid), len(grid[0]), 0

        def dfs(i, j):
            if i==m or j==n or i<0 or j<0:
                return

            if grid[i][j] == "0" or (i, j) in vis:
                return
            
            vis.add((i, j))

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in vis:
                    dfs(i, j)
                    ans += 1
        return ans
        