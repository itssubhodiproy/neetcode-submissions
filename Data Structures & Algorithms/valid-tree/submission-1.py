class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = set()

        if len(edges)!=n-1:
            return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(root):
            if root in vis:
                return
            vis.add(root)
            for node in adj[root]:
                dfs(node)
        
        dfs(0)
        if len(vis)==n:
            return True
        return False
