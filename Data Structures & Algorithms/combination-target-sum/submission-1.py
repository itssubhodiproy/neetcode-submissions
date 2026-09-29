class Solution:
    def rec(self, arr, sum, i, nums, target):
        if i == len(nums) or sum > target:
            return
        if sum==target:
            self.ans.append(arr.copy())
            return
        if sum < target:
            self.rec(arr, sum, i+1, nums, target)
            arr.append(nums[i])
            self.rec(arr, sum+nums[i], i, nums, target)
            arr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans, arr = [], []
        sum, i = 0, 0
        self.rec(arr, sum, i, nums, target)
        return self.ans