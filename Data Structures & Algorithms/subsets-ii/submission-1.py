class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(i, arr):
            if i == len(nums):
                ans.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()

            j = i+1
            while(j<len(nums) and nums[i]==nums[j]):
                j=j+1
            
            backtrack(j, arr)
            
        backtrack(0, [])
        return ans