class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_degree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        ans, q = [], deque()

        for a, b in prerequisites:
            adj[a].append(b)
            in_degree[b] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        def bfs():
            while(q):
                top = q.popleft()
                ans.append(top)
                for ele in adj[top]:
                    in_degree[ele]-=1
                    if in_degree[ele]==0:
                        q.append(ele) 
        bfs()
        ans.reverse()
        
        return ans if len(ans)==numCourses else []
