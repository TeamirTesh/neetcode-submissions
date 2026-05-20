class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            t_count[ord(t[i])-ord('a')] += 1

        if s_count == t_count:
            return True

        return False