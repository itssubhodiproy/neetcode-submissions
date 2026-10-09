class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        vis = set()

        def bfs():
            count = 0

            while(q):
                sz = len(q)
                
                while(sz):
                    i, j = q.popleft()
                
                    directions = [
                            (i + 1, j),
                            (i - 1, j),
                            (i, j + 1),
                            (i, j - 1)
                        ]
                    
                    for row, col in directions:
                        if (
                            row < 0 or row >= m or
                            col < 0 or col >= n or
                            grid[row][col] != 1 or
                            (row, col) in vis
                        ):
                            continue
                        grid[row][col] = 2
                        vis.add((row, col))
                        q.append((row, col))
                    
                    sz-=1
                
                count += 1
            return max(0, count-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i, j))
                    vis.add((i, j))
        
        mins = bfs()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return mins