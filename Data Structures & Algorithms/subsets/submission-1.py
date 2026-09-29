class Solution:

    def rec(self, arr, i, nums):
        if i==len(nums):
            self.ans.append(arr.copy())
            return
        
        self.rec(arr, i+1, nums)
        arr.append(nums[i])
        self.rec(arr, i+1, nums)
        arr.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans, arr = [], []
        self.rec(arr, 0, nums)
        return self.ans
        