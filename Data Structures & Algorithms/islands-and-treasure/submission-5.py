class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        vis = set()
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    vis.add((i, j))
                    queue.append((i, j))
        
        distance = 0

        while(queue):
            sz = len(queue)
            
            for _ in range(sz):
                i, j = queue.popleft()
                grid[i][j] = distance
            
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
                        grid[row][col] == -1 or
                        (row, col) in vis
                    ):
                        continue
                    vis.add((row, col))
                    queue.append((row, col))
            
            distance += 1


        