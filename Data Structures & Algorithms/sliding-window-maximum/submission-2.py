class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        i = 0
        for j in range(len(nums)):
            while(dq and dq[-1][0]<nums[j]):
                dq.pop()
            dq.append((nums[j], j))
            if(dq and dq[0][1]<i):
                dq.popleft()
            if(j-i+1==k):
                ans.append(dq[0][0])
                i+=1
        return ans