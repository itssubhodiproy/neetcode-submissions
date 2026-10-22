class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj, vis, count = [[] for _ in range(n)], set(), 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for chld in adj[node]:
                dfs(chld)

        for i in range(n):
            if i not in vis:
                count += 1
                dfs(i)
        
        return count