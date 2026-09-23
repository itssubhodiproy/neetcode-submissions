class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        i = 0
        for j in range(len(nums)):
            while(dq and nums[dq[-1]]<nums[j]):
                dq.pop()
            dq.append(j)
            while(dq and dq[0]<i):
                dq.popleft()
            if(j-i+1==k):
                ans.append(nums[dq[0]])
                i+=1
        return ans