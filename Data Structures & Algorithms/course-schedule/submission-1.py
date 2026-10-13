class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        vis = [0] * (numCourses)

        for ele in prerequisites:
            adj[ele[0]].append(ele[1])
        
        def dfs(i):
            if vis[i] == 2:
                return False
            
            if vis[i] == 1:
                return True

            vis[i] = 2

            for ele in adj[i]:
                if dfs(ele) == False:
                    return False
            
            vis[i] = 1
            return True


        for i in range(numCourses):
            if vis[i] == 0:
                if dfs(i) == False:
                    return False
        
        return True
            