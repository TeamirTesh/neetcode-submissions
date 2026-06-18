class Solution:
    @staticmethod
    def compute_median(left1, right1, left2, right2, total):
        if total % 2 == 1:
            return min(right1, right2)
        else:
            return (max(left1, left2) + min(right1, right2)) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        l, r = 0, n

        while l <= r:
            mid_1 = (l + r) // 2
            mid_2 = (n + m) // 2 - mid_1

            left1  = nums1[mid_1 - 1] if mid_1 > 0 else float('-inf')
            right1 = nums1[mid_1]     if mid_1 < n else float('inf')
            left2  = nums2[mid_2 - 1] if mid_2 > 0 else float('-inf')
            right2 = nums2[mid_2]     if mid_2 < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                return self.compute_median(left1, right1, left2, right2, n + m)
            elif left1 > right2:
                r = mid_1 - 1
            else:
                l = mid_1 + 1