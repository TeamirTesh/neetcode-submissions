class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        curr = set()
        curr_max = 0

        while r < n:
            if s[r] not in curr:
                curr.add(s[r])
                r += 1
            else:
                curr_max = max(curr_max, len(curr))
                curr.remove(s[l])
                l += 1
        
        curr_max = max(curr_max, len(curr))
                
        return curr_max
            