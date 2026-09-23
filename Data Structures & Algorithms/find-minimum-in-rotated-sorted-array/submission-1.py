class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, mini = 0, len(nums)-1, 1001
        while(l<r):
            m=l+(r-l)//2
            mini = min(mini, nums[m])
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<nums[r]:
                r=m
        return min(mini, nums[l])