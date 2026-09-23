class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i in range(len(nums)):
            if target-nums[i] in bucket:
                return [bucket[target-nums[i]], i]
            bucket[nums[i]]=i
        return[]
