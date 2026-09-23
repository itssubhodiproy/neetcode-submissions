class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        i = 0
        for j in range(len(nums)):
            heapq.heappush(heap, (-nums[j], j))
            while(heap and heap[0][1]<i):
                heapq.heappop(heap)
            if j-i+1 == k:
                ans.append(-heap[0][0])
                i+=1
        return ans