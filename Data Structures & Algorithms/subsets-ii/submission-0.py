class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        bucket = set()
        def backtrack(i, arr):
            if i == len(nums):
                key = tuple(arr)
                if key not in bucket:
                    ans.append(arr.copy())
                    bucket.add(key)
                return
            backtrack(i+1, arr)
            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()
        backtrack(0, [])
        return ans