class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        exclude = 0
        ans = 0

        while r < len(height):
            if height[r] >= height[l]:

                range = r - l - 1

                ans += (height[l] * range) - exclude

                l = r
                r = l + 1
                exclude = 0

            else:
                exclude += height[r]
                r += 1

        # Process the remaining section from right to left
        r = len(height) - 1
        l2 = r - 1
        exclude = 0

        while l2 >= l:
            if height[l2] >= height[r]:

                range = r - l2 - 1

                ans += (height[r] * range) - exclude

                r = l2
                l2 = r - 1
                exclude = 0

            else:
                exclude += height[l2]
                l2 -= 1

        return ans