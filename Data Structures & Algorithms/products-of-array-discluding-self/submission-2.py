class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [0] * n
        right_prod = [0] * n
        ans = [0] * n

        left_prod[0] = nums[0]
        for i in range (1, n):
            left_prod[i] = left_prod[i-1] * nums[i]

        right_prod[n-1] = nums[n-1]
        for i in range (n-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i]
        
        ans[0] = right_prod[1]
        ans[n-1] = left_prod[n-2]

        for i in range (1, n-1):
            ans[i] = left_prod[i-1] * right_prod[i+1]
        return ans
