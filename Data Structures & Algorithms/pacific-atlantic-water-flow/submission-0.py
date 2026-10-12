class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pas_vis, atl_vis, ans = set(), set(), []
        q = deque()

        def bfs(q, vis_set):
            while(q):
                sz = len(q)
                while(sz):
                    i, j = q.popleft()
                    directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                    for row, col in directions:
                        if row < 0 or col < 0 or row == m or col == n:
                            continue
                        if (row, col) in vis_set:
                            continue
                        if heights[row][col] >= heights[i][j]:
                            q.append((row, col))
                            vis_set.add((row, col))
                    sz-=1

        # pacific
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pas_vis.add((i, j))
                    q.append((i, j))

        bfs(q, pas_vis)
        
        # atlantic
        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    atl_vis.add((i, j))
                    q.append((i, j))
        
        bfs(q, atl_vis)
        
        # check
        for i in range(m):
            for j in range(n):
                if (i, j) in pas_vis and (i, j) in atl_vis:
                    ans.append([i, j])
        
        return ans
                
