class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_degree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        ans, q = [], deque()

        for courses in prerequisites:
            adj[courses[0]].append(courses[1])

        for i in range(numCourses):
            for ele in adj[i]:
                in_degree[ele] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        def bfs():
            while(q):
                sz = len(q)
                while(sz):
                    top = q.popleft()
                    ans.append(top)
                    for ele in adj[top]:
                        in_degree[ele]-=1
                        if in_degree[ele]==0:
                            q.append(ele) 
                    sz-=1
        bfs()
        ans.reverse()
        
        return ans if len(ans)==numCourses else []
