class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j = 0, k-1
        n = len(nums)
        result = []

        while j < n:
            curr = max(nums[i:j+1])
            result.append(curr)
            i+=1
            j+=1

        return result