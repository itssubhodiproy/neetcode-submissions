class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range (n):
            mini = 1001
            for j in range (i, n):
                width = j-i+1
                mini = min(mini, heights[j])
                area = max(area, width*mini)
            
        return area
            