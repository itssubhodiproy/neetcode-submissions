class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        m, n, ans = len(grid), len(grid[0]), 0

        def dfs(i, j)-> int:
            if i==m or j==n or i<0 or j<0:
                return 0
            if grid[i][j]==0 or (i, j) in vis:
                return 0
            vis.add((i, j))
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i, j) not in vis:
                    ans = max(ans, dfs(i, j))
        return ans