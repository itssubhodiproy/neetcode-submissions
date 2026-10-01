class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()
        def backtrack(arr):
            if len(arr)==len(nums):
                ans.append(arr.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                arr.append(nums[i])
                used.add(i)
                backtrack(arr)
                arr.pop()
                used.remove(i)
        backtrack([])
        return ans