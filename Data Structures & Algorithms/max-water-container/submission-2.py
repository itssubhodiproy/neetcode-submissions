class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0
        while i < j:
            width = j-i
            vol = width * min(heights[i], heights[j])
            maxi = max(maxi, vol)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxi
