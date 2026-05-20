class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        i = 1
        largest = 0

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 in seen:
                continue

            while num + i in seen:
                i += 1
    
            largest = max(largest, i)
            i = 0

        return largest