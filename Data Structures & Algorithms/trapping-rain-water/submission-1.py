class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        # creating the prefix_arr
        prefix_arr=[0]*n
        prefix_max = 0
        for i in range(n):
            prefix_max = max(height[i], prefix_max)
            prefix_arr[i]=prefix_max
        # creating the suffix_arr
        sufix_arr=[0]*n
        sufix_max=0
        for i in range(n-1, -1, -1):
            sufix_max = max(height[i], sufix_max)
            sufix_arr[i]=sufix_max

        for i in range(n):
            leftMax = prefix_arr[i]
            rightMax = sufix_arr[i]

            water += min(leftMax, rightMax) - height[i]

        return water