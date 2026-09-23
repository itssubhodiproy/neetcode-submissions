class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        for i in range(n):
            leftMax = 0
            rightMax = 0

            # Find highest bar on the left (including current)
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])

            # Find highest bar on the right (including current)
            for j in range(i, n):
                rightMax = max(rightMax, height[j])

            water += min(leftMax, rightMax) - height[i]

        return water