class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        area = 0

        while l < r:
            curr = (r-l) * min(heights[l], heights[r])
            area = max(area, curr)

            if heights[l] > heights[r]:
                r -= 1

            else:
                l += 1
        
        return area