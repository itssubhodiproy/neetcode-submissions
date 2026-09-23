class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, i = [], 0
        while(i<=len(nums)-k):
            maxi = -10001
            j = i
            while(j<i+k):
                maxi = max(maxi, nums[j])
                j+=1
            ans.append(maxi)
            i+=1
        return ans
