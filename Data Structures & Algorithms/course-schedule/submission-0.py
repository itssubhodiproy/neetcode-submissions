class Solution:
    def dfs(self, adjl, vis, node) -> bool:
        if (vis[node]==1):
            return False
        if vis[node]==2:
            return True
        vis[node] = 1
        for ele in adjl[node]:
            if self.dfs(adjl, vis, ele)==False:
                return False
        vis[node] = 2
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjl = [[] for _ in range(numCourses)]
        vis = [0] * numCourses

        for a, b in prerequisites:
            adjl[a].append(b)
        
        for i in range(numCourses):             
            if vis[i] == 0:
                if self.dfs(adjl, vis, i)==False:
                    return False
        
        return True