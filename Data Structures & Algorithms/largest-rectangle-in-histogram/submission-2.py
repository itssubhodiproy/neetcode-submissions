class Solution:
    def nextSmallerElement(self, isRight:bool , nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        indices = range(n - 1, -1, -1) if isRight else range(n)

        for i in indices:
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            elif not stack:
                ans[i] = n if isRight else -1

            stack.append(i)
            
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        
        left_arr = self.nextSmallerElement(False, heights)
        right_arr = self.nextSmallerElement(True, heights)

        for i in range (n):
            width = right_arr[i] - left_arr[i] - 1
            area = max(area, width*heights[i])
        return area
            