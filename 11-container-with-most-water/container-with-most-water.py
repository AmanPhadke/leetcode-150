class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) -1
        max_width = 0

        while l < r:
            if height[l] <= height[r]:
                w = height[l] * (r - l)
                max_width = max(max_width, w)
                l += 1

            else:
                w = height[r] * (r - l)
                max_width = max(max_width, w)
                r -= 1

        return max_width
            