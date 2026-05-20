class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l,r = 0,0
        counts = [0] * 26
        n = len(s1)

        for char in s1:
            counts[ord(char) - ord('a')] += 1

        while l < len(s2):
            while r < len(s2) and counts[ord(s2[r]) - ord('a')] != 0:
                counts[ord(s2[r]) - ord('a')] -= 1
                r += 1
        
            if r - l == n:
                return True

            else:
                counts[ord(s2[l]) - ord('a')] += 1
                l += 1
            
        return False
