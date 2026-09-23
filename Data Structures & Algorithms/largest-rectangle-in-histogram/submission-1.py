class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range (n):
            left_index = i
            right_index = i
            while(left_index>=0 and heights[left_index]>=heights[i]):
                left_index-=1
            while(right_index<n and heights[right_index]>=heights[i]):
                right_index+=1
            width = right_index - left_index - 1
            area = max(area, width*heights[i])
        return area
            