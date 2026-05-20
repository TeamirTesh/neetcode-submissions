class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r, water = 0, n-1, 0
        leftmax, rightmax = 0, 0

        while l < r:
            if height[l] < height[r]:
                if height[l] < leftmax:
                    water += leftmax - height[l]
                else:
                    leftmax = height[l]
                l += 1
            
            else:
                if height[r] < rightmax:
                    water += rightmax - height[r]
                else:
                    rightmax = height[r]
                r -= 1
        return water

