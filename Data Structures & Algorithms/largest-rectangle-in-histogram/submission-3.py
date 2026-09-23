class Solution:
    def nextSmallerIndex(self, searchRight: bool, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        iter_range = range(n - 1, -1, -1) if searchRight else range(n)

        for i in iter_range:
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            else:
                ans[i] = n if searchRight else -1

            stack.append(i)

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = self.nextSmallerIndex(False, heights)
        right = self.nextSmallerIndex(True, heights)

        maxArea = 0

        for i in range(n):
            width = right[i] - left[i] - 1
            maxArea = max(maxArea, width * heights[i])

        return maxArea