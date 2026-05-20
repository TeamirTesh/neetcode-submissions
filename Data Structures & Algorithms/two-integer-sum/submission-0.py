class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            j = target - nums[i]
            if j in seen:
                return [min(i, seen[j]), max(i, seen[j])]
            seen[nums[i]] = i
        